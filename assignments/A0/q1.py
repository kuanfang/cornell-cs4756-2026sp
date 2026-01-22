import numpy as np
import torch

def calculate_distances(x, y):
    """Calculate the Euclidean distances between the vectors in x and y.
    
    Parameters:
        x (numpy.ndarray)
            An array with shape (n, d) where each row corresponds to a vector.
        y (numpy.ndarray)
            An array with shape (n, d) where each row corresponds to a vector.
    
    Returns:
        distances (numpy.ndarray)
            An array with shape (n, 1)
    """
    # TODO: Debug
    diff = x - y
    squared = diff ** 2
    summed = np.sum(squared)
    distances = np.sqrt(summed)
    return distances

def combine_squares(square_1, square_2, square_3, square_4):
    """Concatenate the squares into a combined square.
    
    This function takes in four square tensors and combines them into
    a single square shown below:
        
            -----------------------
            | square_1 | square_2 |
            |----------|----------|
            | square_3 | square_4 |
            -----------------------
    
    Parameters:
        square_1 (torch.Tensor)
            A tensor with shape (n, n)
        square_2 (torch.Tensor)
            A tensor with shape (n, n)
        square_3 (torch.Tensor)
            A tensor with shape (n, n)
        square_4 (torch.Tensor)
            A tensor with shape (n, n)
    
    Returns:
        combined_square (torch.Tensor)
            A tensor with shape (2n, 2n)
    """
    # TODO: Debug
    top = torch.cat((square_1, square_2))
    bottom = torch.cat((square_3, square_4))
    combined_square = torch.cat((top, bottom))
    return combined_square

def video_to_filmstrip(video_frames):
    """Convert video frames into a filmstrip image.
    
    This function takes in a list of numpy arrays where each array
    corresponds to a single frame in a video. The function then
    combines the frames side-by-side into a single image, forming
    a filmstrip. The filmstrip is returned as a tensor.
    
    Parameters:
        video_frames (list of numpy.ndarray)
            A list of numpy arrays with shape (h, w, c)
    
    Returns:
        filmstrip (torch.Tensor)
            A tensor with shape (h, w * n_frames, c)
    """
    # TODO: Implement
    raise NotImplementedError