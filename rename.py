import os 
  
# Function to rename multiple files 
def main():

    for count, filename in enumerate(os.listdir("Path")): 
        try: 
            dst =str(count) + ".jpg"
            src ='your source path'+ filename 
            dst ='your destination path'+ dst 
            
            # rename() function will 
            # rename all the files 
            os.rename(src, dst) 
        except:
            continue
    
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
























# import os 
# #   D:\Dowonload(DECEMBER)\train_data\images\train
# os.chdir('D:/Dowonload(DECEMBER)/train_data/images/train/') 
# print(os.getcwd()) 
# COUNT = 1
  
# # Function to increment count  
# # to make the files sorted. 
# def increment(): 
#     global COUNT 
#     COUNT = COUNT + 1
  
  
# for f in os.listdir(): 
#     f_name, f_ext = os.path.splitext(f) 
#     f_name = str(COUNT) 
#     increment() 
  
#     new_name = '{} {}'.format(f_name, f_ext) 
#     os.rename(f, new_name) 