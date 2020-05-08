import zipfile, os
from pprint import pprint as pp
file_zip = os.path.join('..\\', 'files', 'Automate_the_Boring_Stuff_2e_onlinematerials.zip')


if os.path.exists(file_zip):
    filename, file_extension = os.path.splitext(file_zip)

    if file_extension == '.zip':
        example_zip = zipfile.ZipFile(file_zip)
        pp(example_zip.namelist())
        spam_info = example_zip.getinfo('automate_online-materials/alarm.wav')
        pp(spam_info)
        pp(spam_info.file_size)
        pp(spam_info.compress_size)
        example_zip.extractall()
        example_zip.close()



