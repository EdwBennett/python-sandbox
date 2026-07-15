import re
import sys

def main():
    para = 0
    in_para = False
    sentence = ""
    done = False
    
    filename = "chapter_one.txt"
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove trailing newline character
                line_stripped = line.rstrip('\r\n')
                
                # Check if line is empty (NF == 0 equivalent)
                if not line_stripped.strip():
                    if in_para:
                        para += 1
                        in_para = False
                    continue
                
                if done:
                    continue
                    
                in_para = True
                
                if para == 1:
                    # Append current line plus a space
                    sentence += line_stripped + " "
                    
                    idx = sentence.find('.')
                    if idx != -1:
                        # Take text up to and including the first period
                        out = sentence[:idx + 1]
                        
                        # Remove leading whitespace and collapse multiple spaces to one
                        out = out.lstrip()
                        out = re.sub(r'\s+', ' ', out)
                        
                        print(out)
                        done = True
                        
    except FileNotFoundError:
        print(f"Error: {filename} not found.", file=sys.stderr)

if __name__ == "__main__":
    main()
