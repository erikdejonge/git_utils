import os
def main():

  s = os.popen("ls /home/rabshakeh/workspace/github").read()
  l = s.strip().split("\n")
  f = open("/home/rabshakeh/workspace/git_utils/exclude_dirs", "w")
  for i in l:
    f.write(i)
    f.write("\n")
if __name__=="__main__":
  main()


