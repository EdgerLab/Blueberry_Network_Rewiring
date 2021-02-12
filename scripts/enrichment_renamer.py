import os

# directory = r'C:\Users\admin'
directory = "/home/alder/research/Blueberry_Data/Enrichment_Data/Gene_Analysis"
for folder in os.listdir(directory):
    for files in os.listdir(directory + "/" + folder):
        if files[-1] == "v":
            os.rename(
                directory + "/" + folder + "/" + files,
                directory + "/" + folder + "/" + folder + "_" + files[11:],
            )
        else:
            os.remove(directory + "/" + folder + "/" + files)
