import sys
import numpy as np
import glob

def parse_log_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # Extract the numerical values after the colon
            values = line.split()
            row = [float(values[i].split(':')[1]) for i in range(1, len(values))]
            data.append(row)
    return np.array(data)

def save_matrix(filename, matrix):
    np.savetxt(filename, matrix, fmt='%.2f')

def main():
    # Check if enough arguments are provided
    if len(sys.argv) < 4:
        print("Usage: python3 stats_log.py <input_pattern> <output_prefix> <column_index>")
        sys.exit(1)

    # Get input pattern, output prefix, and desired column index
    input_pattern = sys.argv[1]
    output_prefix = sys.argv[2]
    try:
        column_index = int(sys.argv[3])
    except ValueError:
        print("Error: Column index must be an integer.")
        sys.exit(1)

    # Expand file patterns (e.g., test-*/VIDEO/APSNR/CSP-Scene1-bw50.log)
    file_list = glob.glob(input_pattern)
    
    if not file_list:
        print("Error: No files matched the provided patterns.")
        sys.exit(1)
    
    matrices = []
    for filename in file_list:
        try:
            matrix = parse_log_file(filename)
            matrices.append(matrix)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            sys.exit(1)
    
    # Ensure all matrices are the same shape
    matrix_shape = matrices[0].shape
    if not all(mat.shape == matrix_shape for mat in matrices):
        print("Error: Matrices have different dimensions, cannot calculate statistics.")
        sys.exit(1)
    
    # Stack matrices along a new axis for calculations
    stacked_matrices = np.stack(matrices, axis=0)
    
    # Calculate average, standard deviation, and variance
    avg_matrix = np.mean(stacked_matrices, axis=0)
    stddev_matrix = np.std(stacked_matrices, axis=0)
    variance_matrix = np.var(stacked_matrices, axis=0)
    
    # Save matrices to files
    save_matrix(f"{output_prefix}_avg.txt", avg_matrix)
    save_matrix(f"{output_prefix}_stddev.txt", stddev_matrix)
    save_matrix(f"{output_prefix}_variance.txt", variance_matrix)

    # Check if the column index is within bounds
    if column_index < 0 or column_index >= avg_matrix.shape[1]:
        print(f"Error: Column index {column_index} is out of range.")
        sys.exit(1)
    
    # Calculate and print the average of the specified column
    column_avg = np.mean(avg_matrix[:, column_index])
    # print(f"Average of column {column_index} in the average matrix: {column_avg:.2f}")
    print(f"{column_avg:.4f}", end=" ")    

    # print("Matrices saved:")
    # print(f"  Average: {output_prefix}_avg.txt")
    # print(f"  Standard Deviation: {output_prefix}_stddev.txt")
    # print(f"  Variance: {output_prefix}_variance.txt")

if __name__ == "__main__":
    main()
