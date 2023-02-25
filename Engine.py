import os
import stat


class Formater:
    @staticmethod
    def format_path(folder_path: str | os.PathLike):
        return folder_path.replace("\ "[0], "/")


class Engine:
    @staticmethod
    def check_file_extensions(folder_path: str | os.PathLike):
        extensions = set()

        for object in os.listdir(folder_path):
            full_path = os.path.join(folder_path, object)
            
            if os.path.isfile(full_path):
                file_extension = object.split(".")[1]
                extensions.add(file_extension)
    
        return extensions

    @classmethod
    def sort_folder(cls, folder_path: str | os.PathLike):
        for extension in cls.check_file_extensions(folder_path=folder_path):
            try:
                os.mkdir(os.path.join(folder_path, extension))
            except Exception as e:
                continue
        
        for element in os.listdir(folder_path):
            full_element_path = os.path.join(folder_path, element)

            if os.path.isfile(full_element_path):
                replace_folder_path = full_element_path.split(".")[1]
                os.replace(full_element_path, os.path.join(folder_path, replace_folder_path, element))


