import os

def renamer():
    i = 0 
    path = "C:\\Users\hp\\Documents\\DataScience\\material\\p06\\img\\"
    for filename in os.listdir(path):
        names = f"imag {i}.png"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()

