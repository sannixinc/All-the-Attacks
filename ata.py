#!/usr/bin/python3
import argparse
import pyattck


parser = argparse.ArgumentParser(
    prog="all the attacks",
    description=""
)
attack = pyattck.Attck()

parser.add_argument("tool", help="")

args = parser.parse_args()

def tools():
    file = open("ata.txt", "w")

    for tool in attack.tools:
        if args.tool in tool.name:
            print("tool name: {}".format(tool.name))    
            file.write("Tool name: {}\n".format(tool.name))
                
            for actor in tool.actors:
                print("ACtor Alias: {}".format(actor.aliases))
                file.write("Actor Alias: {}\n".format(actor.aliases))
                
                #for malware in actor.malware:
                    #print("Malware: {}".format(malware.name))
                
    file.close()


if __name__=="__main__":
    tools()
