from zipfile import ZipFile
import os, sys, datetime
def get_all_file_paths(directory):

    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    return file_paths        
  

  
file_paths = get_all_file_paths(sys.argv[2])
zip_name = f'{sys.argv[1]}/{str(datetime.date.today())}.zip'
    
with ZipFile(zip_name,'w') as zip:
    for file in file_paths:
        zip.write(file)

  
  
