class Solution(object):
    def interpret(self, command):
        i = 0
        text = ""
        while i < len(command):
            
            if command[i:i+2] == "()":
                text += "o"
                i += 2
            elif command[i] == "G":
                text += "G"
                i += 1
            elif command[i:i+4] == "(al)":
                text += "al"
                i += 4
        return text
