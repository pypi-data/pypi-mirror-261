# -*- coding: utf-8 -*-


from typing import Tuple
import os
import warnings
from sklearn import preprocessing
import numpy as np
from scipy.signal import resample
import torch
from torch import nn
import __main__
from e2epyppg.utils import find_peaks, resample_signal, get_data, bandpass_filter
from e2epyppg.ppg_sqa import sqa
import more_itertools as mit

warnings.filterwarnings("ignore")


#Maximum reconstruction length (in seconds):
MAX_RECONSTRUCTION_LENGTH_SEC = 15

UPSAMPLING_RATE = 2

RECONSTRUCTION_MODEL_SAMPLING_FREQUENCY = 20

MODEL_PATH = "models"
GAN_MODEL_FILE_NAME = 'GAN_model.pth'

#Define the device
use_gpu = torch.cuda.is_available()

#Define the convolutional encoder structure for generator
encoder1 = nn.Sequential(
    nn.Conv1d(1,32, kernel_size=4, stride = 2, padding = 0,bias=False, padding_mode='replicate'),
    nn.ReLU(),
    nn.Conv1d(32,64, kernel_size = 4, stride =2, padding =0,bias=False, padding_mode='replicate'),
    nn.InstanceNorm1d(64),
    nn.ReLU(),
    nn.Conv1d(64,128, kernel_size = 4, stride =2, padding =0,bias=False, padding_mode='replicate'),
    nn.InstanceNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Conv1d(128,128, kernel_size = 4, stride =2,padding = 0, bias=False),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Conv1d(128,128, kernel_size = 4, stride =2, padding=1, bias=False),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Conv1d(128,128, kernel_size = 4, stride =2, padding=1, bias=False),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Dropout(0.5),
    nn.Dropout(0.5),
)

#Define the second convolutional encoder structure for generator
encoder2 = nn.Sequential(
    nn.Conv1d(1,32, kernel_size=4, stride = 2, padding = 0,bias=False, padding_mode='replicate'),
    nn.ReLU(),
    nn.Conv1d(32,64, kernel_size = 4, stride =2, padding =0,bias=False, padding_mode='replicate'),
    nn.InstanceNorm1d(64),
    nn.ReLU(),
    nn.Conv1d(64,128, kernel_size = 4, stride =2, padding =0,bias=False, padding_mode='replicate'),
    nn.InstanceNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Conv1d(128,128, kernel_size = 4, stride =2,bias=False),
    nn.ReLU(),
    nn.Dropout(0.5)
)

#Define the transposed convolutional decoder structure for generator
decoder = nn.Sequential(
    nn.ConvTranspose1d(128, 128, kernel_size=4, stride=2, output_padding=1, bias=False),
    nn.InstanceNorm1d(128),
    nn.ReLU(inplace=True),
    nn.Dropout(0.5),
    nn.ConvTranspose1d(128, 64, kernel_size=4, stride=2, output_padding=0, bias=False),
    nn.InstanceNorm1d(64),
    nn.ReLU(inplace=True),
    nn.ConvTranspose1d(64, 32, kernel_size=4, stride=2, output_padding=0, bias=False),
    nn.InstanceNorm1d(32),
    nn.ReLU(inplace=True),
)

#Define the generator structure
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        self.encoder1 = encoder1
        self.decoder = decoder
        self.encoder2 = encoder2

        self.final = nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.ConstantPad1d((1, 1), 0),
            nn.Conv1d(32, 1, 4, padding=1,
                      padding_mode='replicate'),
            nn.ReLU(inplace = True)
        ) 
        self.fc1 = nn.Linear(101,100)


    def forward(self,x):
        latent_i = self.encoder1(x)#Apply the first encoder as feature extractor
        gen_img = self.decoder(latent_i)#Reconstruct the signal from latent feature

        #Forward functions for model training purpose
        fin_cov = self.final(gen_img)
        fin_cov = fin_cov.view(256,-1)
        y = self.fc1(fin_cov)
        latent_o = self.encoder2(y.reshape(256,1,-1))
        return y,  latent_o


def gan_rec(
        ppg_clean: np.ndarray,
        noise: list,
        sampling_rate: int,
        generator, device) -> list:
    '''
    Reconstruct noise in the PPG signal using a Generative Adversarial Network (GAN) generator.
    
    This function iteratively reconstructs noise in the PPG signal using a GAN generator.
    The clean signal and reconstructed noise are concatenated, and the process is repeated
    until the entire noise sequence is reconstructed.
    
    Args:
        ppg_clean (np.ndarray): Preceding clean signal to be used for noise reconstruction.
        noise (list): List of noise indices.
        sampling_rate (int): Sampling rate of the PPG signal.
        generator: GAN generator for noise reconstruction.
        device: Device on which to run the generator.
        
    Return:
        reconstructed_noise: The reconstructed noise.

    '''

    # Parameters for reconstruction
    shifting_step = 5
    len_rec = int(shifting_step*sampling_rate)
    reconstructed_noise = []
    remaining_noise = len(noise)

    # Iteratively reconstruct noise
    while(len(reconstructed_noise) < len(noise)):
        # Preprocess and prepare the clean signal for reconstruction
        ppg_clean = preprocessing.scale(ppg_clean)
        y = np.array([np.array(ppg_clean) for i in range(256)])
        ppg_test = torch.FloatTensor(y)

        # Generate reconstructed noise using the GAN generator
        rec_test,_ = generator(ppg_test.reshape(256,1,-1).to(device))
        rec_test = rec_test.cpu()
        noise_rec = rec_test.detach().numpy()[0]

        # Find peaks in the reconstructed noise
        noise_rec_res = resample(noise_rec, int(len(noise_rec) * UPSAMPLING_RATE))
        peaks_rec, _ = find_peaks(noise_rec_res, int(sampling_rate * UPSAMPLING_RATE))

        # Find peaks in the clean signal
        ppg_resampled = resample(ppg_clean, int(len(ppg_clean) * UPSAMPLING_RATE))
        peaks_ppg, _ = find_peaks(ppg_resampled, int(sampling_rate * UPSAMPLING_RATE))

        # Concatenate reconstructed noise with preceding clean signal
        ppg_and_rec = list(ppg_resampled[:peaks_ppg[-1]]) + list(noise_rec_res[peaks_rec[0]:])

        len_ppg_and_rec = len(ppg_clean) + len(noise_rec)

        # Resample to the original length of the clean signal and reconstructed noise
        ppg_and_rec_down = resample(ppg_and_rec, len_ppg_and_rec)

        # Update reconstructed noise based on the remaining noise
        if remaining_noise < (len_rec):
            reconstructed_noise = reconstructed_noise + list(
                ppg_and_rec_down[len(ppg_clean):int((len(ppg_clean)+remaining_noise))])
        else:
            # Select the reconstructed part of the signal
            reconstructed_noise = reconstructed_noise + list(
                ppg_and_rec_down[len(ppg_clean):(len(ppg_clean)+int(len_rec))])
            # Update remaining noise value
            remaining_noise = remaining_noise - (len_rec)

        # Select the next segment of the clean signal for the next iteration (next reconstruction)
        ppg_clean = ppg_and_rec_down[int(len_rec):len(ppg_clean)+int(len_rec)]

    return reconstructed_noise


def reconstruction(
        sig: np.ndarray,
        clean_indices: list,
        noisy_indices:list,
        sampling_rate: int,
        filter_signal: bool = True,
) -> Tuple[np.ndarray, list, list]:
    '''
    Reconstruct noisy PPG signals using GAN.

    Args:
        sig (np.ndarray): Original PPG signal.
        clean_indices (list): List of indices representing clean parts.
        noisy_indices (list): List of indices representing noisy parts.
        sampling_rate (int): Sampling rate of the signal.
        filter_signal (bool): True if the signal has not filtered using
            a bandpass filter.

    Return:
        ppg_signal (np.ndarray): Reconstructed PPG signal (if reconstruction is
            applied; otherwise, returns the original signal).
        clean_indices (list): Updated indices of clean parts (if reconstruction is
            applied; otherwise, returns the original indices of clean parts).
        noisy_indices (list): Updated indices of noisy parts (if reconstruction is
            applied; otherwise, returns the original indices of noisy parts).
    
    Reference:
        Wang, Y., Azimi, I., Kazemi, K., Rahmani, A. M., & Liljeberg, P. (2022, July). 
        Ppg signal reconstruction using deep convolutional generative adversarial network. 
        In 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (pp. 3387-3391). IEEE.

    '''

    # Set the Generator class in the main module for compatibility with the saved GAN model
    setattr(__main__, "Generator", Generator)

    # Load GAN model parameters
    this_dir, this_filename = os.path.split(__file__)
    generator = torch.load(os.path.join(
        this_dir, MODEL_PATH, GAN_MODEL_FILE_NAME), map_location=torch.device('cpu'))
    device = torch.device(
        "cuda:0" if torch.cuda.is_available() else "cpu")

    resampling_flag = False
    # Check if resampling is needed and perform resampling if necessary
    if sampling_rate != RECONSTRUCTION_MODEL_SAMPLING_FREQUENCY:
        sig = resample_signal(
            sig=sig, fs_origin=sampling_rate, fs_target=RECONSTRUCTION_MODEL_SAMPLING_FREQUENCY)
        resampling_flag = True
        resampling_rate = sampling_rate/RECONSTRUCTION_MODEL_SAMPLING_FREQUENCY
        sampling_rate_original = sampling_rate
        sampling_rate = RECONSTRUCTION_MODEL_SAMPLING_FREQUENCY
        
        # Update clean indices according to the new sampling rate
        clean_indices = [list(range(int(sublist[0]/resampling_rate), int(sublist[-1]/resampling_rate)+1)) for sublist in clean_indices]
        
        # Flatten the clean indices
        clean_indices = [item for sublist in clean_indices for item in sublist]
        
        signal_length_res = len(sig)
        signal_indices_res = list(range(signal_length_res))
        
        # The indices that dont exist in the flat list of clean indices indicate noisy indices    
        noisy_indices_flat = [item for item in signal_indices_res if item not in clean_indices]
        
        # Unflat the noisy indices list to separte noisy parts
        noisy_indices = []
        for group in mit.consecutive_groups(noisy_indices_flat):
            noisy_indices.append(list(group))
            
    else:
        # Flatten the clean indices list
        clean_indices = [item for sublist in clean_indices for item in sublist]

    # Apply bandpass filter if needed
    if filter_signal:
        sig = bandpass_filter(
            sig=sig, fs=sampling_rate, lowcut=0.5, highcut=3)

    # Scale the original PPG signal for further processing
    sig_scaled= preprocessing.scale(sig)

    # Maximum length for reconstruction
    max_rec_length = int(MAX_RECONSTRUCTION_LENGTH_SEC*sampling_rate)

    # Flag to indicate if reconstruction has occurred
    reconstruction_flag = False

    # Iterate over noisy parts for reconstruction
    for noise in noisy_indices:
        if len(noise) <= max_rec_length:
            noise_start_idx = noise[0]
            # Check if there is sufficient preceding clean signal for reconstruction
            if noise_start_idx >= max_rec_length:
                # Check if the preceding signal is clean
                if set(range(
                    noise_start_idx - max_rec_length,
                    noise_start_idx)).issubset(clean_indices):
                    # Perform noise reconstruction for the current noise
                    reconstructed_noise = gan_rec(
                        sig[noise_start_idx-max_rec_length:noise_start_idx],
                        noise, sampling_rate, generator, device)

                    # Upsample the reconstructed noise
                    reconstructed_noise_res = resample(
                        reconstructed_noise,
                        int(len(reconstructed_noise)*UPSAMPLING_RATE))

                    # Upsample the clean signal before the noise
                    sig_before_noise_res = resample(
                        sig_scaled[:noise_start_idx],
                        int(len(sig_scaled[:noise_start_idx])*UPSAMPLING_RATE))

                    # Upsample the clean signal after the noise
                    sig_after_noise_res = resample(
                        sig_scaled[noise[-1]:],
                        int(len(sig_scaled[noise[-1]:])*UPSAMPLING_RATE))

                    # Find peaks in the clean signal before the noise
                    peaks_sig_before_noise, _ = find_peaks(
                        sig_before_noise_res,
                        int(sampling_rate*UPSAMPLING_RATE))

                    # Check if the reconstructed noise is long enough
                    #   (considering a threshold of 2 seconds)
                    if len(reconstructed_noise_res) >= 2*sampling_rate*UPSAMPLING_RATE:
                        try:
                            # Find peaks in the reconstructed noise
                            peaks_noise_rec, _ = find_peaks(
                                reconstructed_noise_res,
                                int(sampling_rate*UPSAMPLING_RATE))

                            # Check if the clean signal after the noise is long enough
                            #   (considering a threshold of 2 seconds)
                            if len(sig_after_noise_res) >= 2*sampling_rate*UPSAMPLING_RATE:
                                # Find peaks in the clean signal after the noise
                                peaks_sig_after_noise, _ = find_peaks(
                                    sig_after_noise_res,
                                    int(sampling_rate*UPSAMPLING_RATE))

                                # Merge the reconstructed noise with the clean signal
                                sig_res = list(sig_before_noise_res[:peaks_sig_before_noise[-1]]) + \
                                list(reconstructed_noise_res[peaks_noise_rec[0]:peaks_noise_rec[-1]]) + \
                                list(sig_after_noise_res[peaks_sig_after_noise[0]:])

                            # If the clean signal after the noise is too short, there is no need
                            #   for peak detection
                            else:
                                # Merge the reconstructed noise with the clean signal
                                sig_res = list(sig_before_noise_res[:peaks_sig_before_noise[-1]]) + \
                                list(reconstructed_noise_res[peaks_noise_rec[0]:peaks_noise_rec[-1]]) + \
                                list(sig_after_noise_res)
                        except:
                            continue

                    else:
                        try:
                            # Check if the clean signal after the noise is long enough
                            #   (considering a threshold of 2 seconds)
                            if len(sig_after_noise_res) >= 2*sampling_rate*UPSAMPLING_RATE:
                                # Find peaks in the clean signal after the noise
                                peaks_sig_after_noise, _ = find_peaks(
                                    sig_after_noise_res,
                                    int(sampling_rate*UPSAMPLING_RATE))

                                # Merge the reconstructed noise with the clean signal
                                sig_res = list(sig_before_noise_res[:peaks_sig_before_noise[-1]]) + \
                                list(reconstructed_noise_res) + \
                                list(sig_after_noise_res[peaks_sig_after_noise[0]:])

                            # If the clean signal after the noise is too short, there is no need
                            #   for peak detection
                            else:
                                # Merge the reconstructed noise with the clean signal
                                sig_res = list(sig_before_noise_res[:peaks_sig_before_noise[-1]]) + \
                                list(reconstructed_noise_res) + \
                                list(sig_after_noise_res)
                        except:
                            continue

                    # Resample the reconstructed signal to the original length of the signal
                    sig_scaled= resample(sig_res, len(sig_scaled))

                    # Descale the reconstructed signal
                    ppg_descaled = (sig_scaled*np.std(sig)) + np.mean(sig)

                    # Set the reconstruction flag to True
                    reconstruction_flag = True

                    # Perform the signal quality assessment to ensure that the reconstructed
                    #   signal is not distorted
                    clean_indices, noisy_indices = sqa(
                        sig=ppg_descaled, sampling_rate=sampling_rate, filter_signal=False)
                    
                    # Flatten the clean indices list
                    clean_indices = [item for sublist in clean_indices for item in sublist]

    # Check if there was a reconstruction
    if reconstruction_flag:
        ppg_signal = ppg_descaled
    else:
        ppg_signal = sig
        
    # If resampling performed, update the reconstructed signal and indices according to the original sampling rate
    if resampling_flag:
        
        # Resample the reconstructed signal according to the original sampling rate
        ppg_signal = resample_signal(
            sig=ppg_signal, fs_origin=sampling_rate, fs_target=sampling_rate_original)
        
        signal_length = len(ppg_signal)
        signal_indices = list(range(signal_length))
        
        # Unflat the clean indices list to create a list of list of clean indices
        clean_indices_unflat = []
        for group in mit.consecutive_groups(clean_indices):
            clean_indices_unflat.append(list(group))
            
        # Update clean indices according to the original sampling rate
        clean_indices = [list(range(int(sublist[0]*resampling_rate), int(sublist[-1]*resampling_rate)+1)) for sublist in clean_indices_unflat]
        
        # Flatten the clean indices
        clean_indices = [item for sublist in clean_indices for item in sublist]
        
        # The indices that dont exist in the flat list of clean indices indicate noisy indices    
        noisy_indices = [item for item in signal_indices if item not in clean_indices]
        
        # Unflat the clean indices list to separte clean parts
        clean_indices_unflat = []
        for group in mit.consecutive_groups(clean_indices):
            clean_indices_unflat.append(list(group))
        clean_indices = clean_indices_unflat
        
        # Unflat the noisy indices list to separte noisy parts
        noisy_indices_unflat = []
        for group in mit.consecutive_groups(noisy_indices):
            noisy_indices_unflat.append(list(group))
        noisy_indices = noisy_indices_unflat
        
            
    else:
        # Unflat the clean indices list to separte clean parts
        clean_indices_unflat = []
        for group in mit.consecutive_groups(clean_indices):
            clean_indices_unflat.append(list(group))
        clean_indices = clean_indices_unflat
    
    
    # Return the reconstructed or original PPG signal, along with updated indices
    return ppg_signal, clean_indices, noisy_indices


if __name__ == "__main__":
    # Import a sample data
    file_name = "201902020222_Data.csv"
    input_sampling_rate = 20
    input_sig = get_data(file_name=file_name)

    # Run PPG signal quality assessment.
    clean_ind, noisy_ind = sqa(sig=input_sig, sampling_rate=input_sampling_rate)

    # Run PPG reconstruction
    reconstructed_signal, clean_ind, noisy_ind = reconstruction(
        sig=input_sig,
        clean_indices=clean_ind,
        noisy_indices=noisy_ind,
        sampling_rate=input_sampling_rate)

    # Display results
    print("Analysis Results:")
    print("------------------")
    print(f"Number of clean parts in the signal after reconstruction: {len(clean_ind)}")
    if clean_ind:
        print("Length of each clean part in the signal (in seconds):")
        for clean_seg in clean_ind:
            print(f"   - {len(clean_seg)/input_sampling_rate:.2f}")
                    
    print(f"Number of noisy parts in the signal after reconstruction: {len(noisy_ind)}")
    if noisy_ind:
        print("Length of each noise in the signal (in seconds):")
        for noise in noisy_ind:
            print(f"   - {len(noise)/input_sampling_rate:.2f}")
