class Solution:
    def simplifyPath(self, path: str) -> str:
        simple_path = path.split("/")

        simplified_Path = []

        for p in simple_path:
            if simplified_Path and p == "..":
                simplified_Path.pop()
            elif p and p != '.' and p != "..":
                simplified_Path.append(p)
        
        return "/" + "/".join(simplified_Path)