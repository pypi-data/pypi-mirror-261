# pyawd - Marmousi
# Tribel Pascal - pascal.tribel@ulb.be
"""
Gathers functions to generate videos from a given simulation.
"""
from typing import Tuple, List, Dict

import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
from glob import glob
import numpy as np
from subprocess import call
from os import remove
from tqdm.auto import tqdm
from devito import Function
import pyvista as pv

from pyawd.utils import get_black_cmap, get_white_cmap

COLORS = TABLEAU_COLORS


def generate_video(img: np.ndarray, interrogators: List[Tuple] = None,
                   interrogators_data: Dict[Tuple, List] = None,
                   name: str = "test", nx: int = 32, dt: float = 0.01, c: Function = None, verbose: bool = False):
    """
    Generates a video from a sequence of images, with a scalar value on each point.
    Args:
        img (numpy.ndarray): A sequence of np.arrays containing the wave state at every timestep
        interrogators (List[Tuple]): A list containing the coordinates of each interrogator, as tuples
        interrogators_data (Dict[Tuple, List]): Couples of interrogators coordinates associated with their measured data
        name (str): The name of the file to save the data to, without the `.mp4` extension
        nx (int): The width of the plane to display (it is assumed to be a squared plane)
        dt (float): The size of the timestep between two subsequent images
        c (devito.Function): A function of space representing the wave propagation speed in each spatial point
        verbose (bool): Gives information about the video generation
    """
    colors = {}
    i = 0
    if interrogators:
        for interrogator in interrogators:
            colors[interrogator] = list(COLORS.values())[i]
            i += 1
    if verbose:
        print("Generating", len(img), "images and saving to " + name + ".mp4.")
    for i in tqdm(range(len(img))):
        if interrogators:
            fig, ax = plt.subplots(ncols=2, figsize=(10, 5), gridspec_kw={'width_ratios': [1, 1]})
            if c:
                ax[0].imshow(c.data.T, vmin=np.min(c.data), vmax=np.max(c.data), cmap="gray")
            im = ax[0].imshow(img[i].T, cmap=get_black_cmap(), vmin=-np.max(np.abs(img[i:])),
                              vmax=np.max(np.abs(img[i:])))
            plt.colorbar(im, shrink=0.75, ax=ax[0])
        else:
            fig, ax = plt.subplots(figsize=(5, 5), gridspec_kw={'width_ratios': [1]})
            if c:
                ax.imshow(c.data.T, vmin=np.min(c.data), vmax=np.max(c.data), cmap="gray")
            im = ax.imshow(img[i].T, cmap=get_black_cmap(), vmin=-np.max(np.abs(img[i:])), vmax=np.max(np.abs(img[i:])))
            ax.axis('off')
            plt.colorbar(im, shrink=0.75, ax=ax)
        if interrogators:
            for interrogator in interrogators:
                ax[0].scatter(interrogator[0] + (nx // 2), -interrogator[1] + (nx // 2), marker="1",
                              color=colors[interrogator])
                ax[1].plot(np.arange(0, len(img) * dt, dt)[:i + 1], interrogators_data[interrogator][:i + 1],
                           color=colors[interrogator])
            ax[1].set_xlabel("Time")
            ax[1].set_ylabel("Amplitude")
            ax[1].legend([str(i) for i in interrogators_data])
            ax[1].set_ylim((np.min(np.array(list(interrogators_data.values()))),
                            np.max(np.array(list(interrogators_data.values())))))
            ax[0].axis('off')
        plt.title("t = " + str(dt * i)[:4] + "s")
        plt.savefig(name + "%02d.png" % i, dpi=250)
        plt.close()

    call([
        'ffmpeg', '-loglevel', 'panic', '-framerate', str(int(1 / dt)), '-i', name + '%02d.png', '-r', '32', '-pix_fmt',
        'yuv420p', name + ".mp4", '-y'
    ])
    for file_name in glob(name + "*.png"):
        remove(file_name)


def generate_quiver_video(quiver_x: np.ndarray, quiver_y: np.ndarray, quiver_z: np.ndarray = None, interrogators: List[Tuple] = None,
                          interrogators_data: Dict[Tuple, List] = None, name: str = "test", nx: int = 32, dt: float = 0.01,
                          c: Function = None, max_velocity: np.ndarray = 0, dim: int = 2,verbose: bool = False):
    """
    Generates a video from a sequence of images, with a vector value on each point.
    Args:
        quiver_x (numpy.ndarray): A sequence of np.arrays containing the wave x vector coordinate at every timestep
        quiver_y (numpy.ndarray): A sequence of np.arrays containing the wave y vector coordinate at every timestep
        quiver_z (numpy.ndarray): A sequence of np.arrays containing the wave z vector coordinate at every timestep
        interrogators (List[Tuple]): A list containing the coordinates of each interrogator, as tuples
        interrogators_data (Dict[Tuple, List]): Couples of interrogators coordinates associated with their measured data
        name (str): The name of the file to save the data to, without the `.mp4` extension
        nx (int): The width of the plane to display (it is assumed to be a squared plane)
        dt (float): The size of the timestep between two subsequent images
        c (devito.Function): A function of space representing the wave propagation speed in each spatial point
        max_velocity (np.ndarray): The maximal speed of propagation
        dim (int): The number of dimensions of the simulations (2 or 3)
        verbose (bool): Gives information about the video generation
    """
    if dim == 3:
        print("Quiver video is only available in 2D.")
    if dim == 2:
        if c is None:
            c = []
        colors = {}
        i = 0
        if interrogators:
            for interrogator in interrogators:
                colors[interrogator] = list(COLORS.values())[i]
                i += 1
        if verbose:
            print("Generating", len(quiver_x), "images.")
        for i in tqdm(range(len(quiver_x))):
            fig = plt.figure()
            a, b = np.meshgrid(np.arange(nx), np.arange(nx))
            ax = fig.add_subplot(1, 1, 1)
            ax.imshow(c.data[:], vmin=np.min(c.data[:]), vmax=np.max(c.data[:]), cmap="gray")
            ax.quiver(a, b, quiver_x[i], -quiver_y[i], scale=0.25)
            for interrogator in interrogators:
                ax.scatter(interrogator[0] + (nx // 2), interrogator[1] + (nx // 2), marker="1",
                              color=colors[interrogator])
            ax.set_title("t = " + str(i * dt) + "s")
            ax.axis("off")
            fig.suptitle("t = " + str(dt * i)[:4] + "s, velocity factor = " + str(max_velocity)[:5])
            plt.tight_layout()
            plt.savefig(name + "%02d.png" % i, dpi=250)
            plt.close()

        call([
            'ffmpeg', '-loglevel', 'panic', '-framerate', str(int(1 / dt)), '-i', name + '%02d.png', '-r', '32', '-pix_fmt',
            'yuv420p', name + ".mp4", '-y'
        ])
        for file_name in glob(name + "*.png"):
            remove(file_name)


import pyvista as pv


def generate_density_video(quiver_x: np.ndarray, quiver_y: np.ndarray, quiver_z: np.ndarray,
                           interrogators: List[Tuple] = None,
                           interrogators_data: Dict[Tuple, List] = None, name: str = "test", nx: int = 32,
                           dt: float = 0.01,
                           c: Function = None, max_velocity: np.ndarray = 0, verbose: bool = False):
    """
    Generates a video from a sequence of images, with a vector value on each point.
    Args:
        quiver_x (numpy.ndarray): A sequence of np.arrays containing the wave x vector coordinate at every timestep
        quiver_y (numpy.ndarray): A sequence of np.arrays containing the wave y vector coordinate at every timestep
        quiver_z (numpy.ndarray): A sequence of np.arrays containing the wave z vector coordinate at every timestep
        interrogators (List[Tuple]): A list containing the coordinates of each interrogator, as tuples
        interrogators_data (Dict[Tuple, List]): Couples of interrogators coordinates associated with their measured data
        name (str): The name of the file to save the data to, without the `.mp4` extension
        nx (int): The width of the plane to display (it is assumed to be a squared plane)
        dt (float): The size of the timestep between two subsequent images
        c (devito.Function): A function of space representing the wave propagation speed in each spatial point
        max_velocity (np.ndarray): The maximal speed of propagation
        verbose (bool): Gives information about the video generation
    """
    lengths = np.sqrt(quiver_x**2 + quiver_y**2 + quiver_z**2)
    p = pv.Plotter(shape=(1, 1), notebook=False, off_screen=True)
    grid = pv.ImageData()
    grid.dimensions = np.array(lengths[0].shape) + 1
    grid.cell_data["values"] = lengths[0].flatten(order="F")
    p.add_mesh(grid, clim=[-np.max(np.abs(lengths)), np.max(np.abs(lengths))], cmap=get_white_cmap())
    p.open_movie(name+".mp4")
    for i in tqdm(range(len(quiver_x))):
        values = lengths[i]
        grid.cell_data["values"] = values.flatten(order="F")
        p.write_frame()
    p.close()