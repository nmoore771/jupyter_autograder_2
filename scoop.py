import sys
import json

print(sys.argv)

# Load the notebook file
with open(sys.argv[2], "r") as fh :
    file = json.load(fh)
    for cell in file["cells"] :
        if ("nbgrader" in cell["metadata"].keys()) :
            #print(cell["metadata"]["nbgrader"]["grade_id"])
            if (cell["metadata"]["nbgrader"]["grade_id"] == sys.argv[1]):
                print("Target Acquired.")
                
                code = cell["source"]
                print("Injecting Postcondition... " + sys.argv[3])
                
                i = 0
                while i < len(code) :
                    if "[POSTCONDITION TAG]" in code[i]:
                        code[i] = "\tassert(" + sys.argv[3] + ");\n"
                    i += 1
                        
                preconds = sys.argv[4:]
                    
                print("Injecting Preconditions... " + str(preconds))
                
                i = 0
                while i < len(code) :
                    if "[PRECONDITION TAG]" in code[i]:
                        code[i] = ""
                        for cond in preconds:
                            code[i] = code[i] + "\t" + cond + ";\n"
                    i += 1
                
                with open("answer.c", "w") as fh2 :
                    fh2.writelines(code)
                break 
            