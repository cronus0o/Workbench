# Virtual Shell

import os
import shutil

class VirtualShell :
    def __init__(self, user_name) :
        self.user_name = user_name
        self.root_dir = os.path.abspath(f"vroot_{self.user_name}")
        os.makedirs(self.root_dir, exist_ok=True)
        self.cwd = self.root_dir

    def _abs_path(self, path) :
        if path.startswith("/") :
            abs_path = os.path.join(self.root_dir, path.lstrip("/"))
        else :
            abs_path = os.path.join(self.cwd, path)
        abs_path = os.path.abspath(abs_path)
        if not abs_path.startswith(self.root_dir) :
            raise ValueError("Access denied: outside of user root")
        return abs_path

    def mkdir(self, path) :
        try :
            os.makedirs(self._abs_path(path), exist_ok=False)
            return ""
        except FileExistsError :
            return f"mkdir: cannot create directory '{path}': File exists"
        except ValueError as e :
            return f"mkdir: {e}"

    def ls(self, path="") :
        try :
            target = self._abs_path(path) if path else self.cwd
            return "     ".join(sorted(os.listdir(target)))
        except FileNotFoundError :
            return f"ls: cannot access '{path}': No such file or directory"

    def cd(self, path) :
        try :
            new_path = self._abs_path(path)
            if not os.path.isdir(new_path) :
                return f"cd: {path}: Not a directory"
            self.cwd = new_path
            return ""
        except ValueError as e :
            return f"cd: {e}"

    def pwd(self) :
        rel = os.path.relpath(self.cwd, self.root_dir)
        return "/" if rel == "." else "/" + rel.replace("\\", "/")

    def mv(self, src, dst) :
        try :
            src_path = self._abs_path(src)
            dst_path = self._abs_path(dst)
            shutil.move(src_path, dst_path)
            return ""
        except FileNotFoundError :
            return f"mv: cannot stat '{src}': No such file or directory"
        except ValueError as e :
            return f"mv: {e}"

    def rm(self, path) :
        try :
            target = self._abs_path(path)
            if os.path.isdir(target) :
                os.rmdir(target)
            else :
                os.remove(target)
            return ""
        except FileNotFoundError :
            return f"rm: cannot remove '{path}': No such file or directory"
        except OSError :
            return f"rm: cannot remove '{path}': Directory not empty"
        except ValueError as e :
            return f"rm: {e}"

    def basicDirectory(self) :
        self.mkdir("home")
        self.mkdir("bin")
        self.mkdir("var")
        self.mkdir("mnt")
        self.mkdir("sys")
        self.cd("home")
        self.mkdir(self.user_name)
        self.cd(self.user_name)
        self.mkdir("Desktop")
        self.mkdir("Downloads")
        self.mkdir("Documents")

if __name__ == "__main__" :
    user_name = "test"
    vsh = VirtualShell(user_name)
    vsh.basicDirectory()
