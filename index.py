import subprocess
import re
def syntax(text):
    p=subprocess.Popen("docker run --name mfdcaparsefc --rm -i  brianlow/syntaxnet-docker bash",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    out=p.communicate("echo '"+text+"' | syntaxnet/demo.sh")
    file=open("out.txt", "w")
    file.write(str(out))

#syntax("Bob, a resident of Yorkshire, loves his wife and children")
