#Write a program to print Twinkle twinkle little star poem in python
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.'''),



#Write a python program to print the contents of a directory using the os module.Search online for the function which does that. 
import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing '{directory}'.")

if __name__ == "__main__":
    # Specify the directory you want to list
    directory_path = '/Aman'
    print_directory_contents(directory_path)
