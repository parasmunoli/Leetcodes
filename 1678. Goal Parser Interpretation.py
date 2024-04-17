def interpret(command):
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command
    
command = "G()(al)"
print(interpret(command))