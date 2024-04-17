def find_longest_common_subsequences(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D table to store the lengths of longest common subsequences
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]

    # Compute the lengths of longest common subsequences
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(
                    lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

    # Find all the longest common subsequences
    subsequences = []
    find_subsequences(str1, str2, m, n, lcs_lengths, "", subsequences)

    # Print the longest common subsequences
    for subsequence in subsequences:
        print(subsequence)


def find_subsequences(str1, str2, i, j, lcs_lengths, current_subsequence, subsequences):
    if i == 0 or j == 0:
        subsequences.append(current_subsequence[::-1])
        return

    if str1[i - 1] == str2[j - 1]:
        find_subsequences(str1, str2, i - 1, j - 1, lcs_lengths,
                          str1[i - 1] + current_subsequence, subsequences)
    elif lcs_lengths[i - 1][j] >= lcs_lengths[i][j - 1]:
        find_subsequences(str1, str2, i - 1, j, lcs_lengths,
                          current_subsequence, subsequences)
    else:
        find_subsequences(str1, str2, i, j - 1, lcs_lengths,
                          current_subsequence, subsequences)


# Test the function
str1 = """Feedforward Neural Networks (FNNs):
Structure: These networks consist of an input layer, one or more hidden layers, and an output layer. Information flows in one direction (from input to output).
Applications:
Image Classification: Identifying objects in images (e.g., recognizing cats or dogs).
Natural Language Processing (NLP): Sentiment analysis, text classification, and language modeling.

Convolutional Neural Networks (CNNs):
Structure: Designed for processing grid-like data (such as images).
Applications:
Image Recognition: Detecting patterns and features in images.
Object Detection: Locating and identifying objects within an image.

Recurrent Neural Networks (RNNs):
Structure: Loops allow information to persist across different time steps.
Applications:
Sequence-to-Sequence Tasks: Machine translation, speech recognition.
Time Series Prediction: Stock market forecasting, weather prediction.

Long Short-Term Memory Networks (LSTMs):
Structure: A type of RNN with memory cells that can store information over long sequences.
Applications:
Natural Language Understanding: Text generation, chatbots.
Speech Recognition: Converting spoken language to text.
Gated Recurrent Units (GRUs):
Structure: Similar to LSTMs but with fewer parameters.
Applications:
Language Modeling: Predicting the next word in a sentence.
Recommendation Systems: Personalized content recommendations.
Autoencoders:
Structure: Comprised of an encoder and a decoder.
Applications:
Dimensionality Reduction: Feature extraction, anomaly detection.
Image Denoising: Removing noise from images.
Generative Adversarial Networks (GANs):
Structure: Consists of a generator and a discriminator.
Applications:
Image Generation: Creating realistic images from random noise.
Style Transfer: Transforming images in the style of famous artists.
Radial Basis Function (RBF) Networks:
Structure: Utilizes radial basis functions for activation.
Applications:
Function Approximation: Interpolating data points.
Pattern Recognition: Identifying complex patterns.
Self-Organizing Maps (SOMs):
Structure: Organizes data into a low-dimensional grid.
Applications:
Clustering: Grouping similar data points.
Visualization: Displaying high-dimensional data in 2D or 3D.
Modular Neural Networks:
Structure: Composed of multiple interconnected subnetworks (modules).
Applications:
Hierarchical Learning: Combining specialized modules for complex tasks."""
str2 = """Feedforward Neural Networks (FNNs):
Structure: These networks consist of an input layer, one or more hidden layers, and an output layer. Information flows in one direction (from input to output).
Applications:
Image Classification: Identifying objects in images (e.g., recognizing cats or dogs).
Natural Language Processing (NLP): Sentiment analysis, text classification, and language modeling.

Convolutional Neural Networks (CNNs):
Structure: Designed for processing grid-like data (such as images).
Applications:
Image Recognition: Detecting patterns and features in images.
Object Detection: Locating and identifying objects within an image.

Recurrent Neural Networks (RNNs):
Structure: Loops allow information to persist across different time steps.
Applications:
Sequence-to-Sequence Tasks: Machine translation, speech recognition.
Time Series Prediction: Stock market forecasting, weather prediction.

Long Short-Term Memory Networks (LSTMs):
Structure: A type of RNN with memory cells that can store information over long sequences.
Applications:
Natural Language Understanding: Text generation, chatbots.
Speech Recognition: Converting spoken language to text.
Gated Recurrent Units (GRUs):
Structure: Similar to LSTMs but with fewer parameters.
Applications:
Language Modeling: Predicting the next word in a sentence.
Recommendation Systems: Personalized content recommendations.
Autoencoders:
Structure: Comprised of an encoder and a decoder.
Applications:
Dimensionality Reduction: Feature extraction, anomaly detection.
Image Denoising: Removing noise from images.
Generative Adversarial Networks (GANs):
Structure: Consists of a generator and a discriminator.
Applications:
Image Generation: Creating realistic images from random noise.
Style Transfer: Transforming images in the style of famous artists.
Radial Basis Function (RBF) Networks:
Structure: Utilizes radial basis functions for activation.
Applications:
Function Approximation: Interpolating data points.
Pattern Recognition: Identifying complex patterns.
Self-Organizing Maps (SOMs):
Structure: Organizes data into a low-dimensional grid.
Applications:
Clustering: Grouping similar data points.
Visualization: Displaying high-dimensional data in 2D or 3D.
Modular Neural Networks:
Structure: Composed of multiple interconnected subnetworks (modules).
Applications:
Hierarchical Learning: Combining specialized modules for complex tasks."""
find_longest_common_subsequences(str1, str2)
