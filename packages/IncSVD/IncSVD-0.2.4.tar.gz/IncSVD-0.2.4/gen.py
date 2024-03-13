import sys
import re
import base64
import chardet

images_suffix = ["gif", "png", "jpg", "jpeg"]

appendix = []

def transform(lines):
    newlines = []
    pattern = re.compile(r'!\[(.*)\]\((.*)\)', re.I) # 正则匹配
    for line in lines:
        li = pattern.findall(line)
        if not li:
            newlines.append(line)
            continue
        for match in li:
            img_name = match[0]
            img_path = match[1]
            if not img_name or not img_path:
                newlines.append(line)
                continue
            if 'http' in img_path: # skip http img
                newlines.append(line)
                continue
            suffix = img_path.rsplit(".")[1]
            if suffix in images_suffix:
                try:
                    with open(img_path, 'rb') as f:
                        image_bytes = base64.b64encode(f.read())
                except:
                    newlines.append(line)
                    continue
                image_str = str(image_bytes)
                #print(image_str)
                base64_pre = 'data:image/' + suffix + ';base64,'
                real_image_str = base64_pre + image_str[2:len(image_str) - 1]
                appendix.append('[' + img_name + ']' + ':' + real_image_str + '\n\n\n')
                line = line.replace('(' + img_path + ')', '[' + img_name + ']')
        newlines.append(line)    
                
    return newlines

def md_2_img(markdown_file):
    if not markdown_file.endswith('.md'):
        return
    code = chardet.detect(open(markdown_file, 'rb').read())['encoding']
    with open(markdown_file, 'r',  encoding=code) as mk:
        lines = mk.readlines()
    newlines = transform(lines)
    with open(markdown_file, 'w',  encoding=code) as mk:
        mk.writelines(newlines)
    with open(markdown_file, 'a+',  encoding=code) as mk:
        mk.write("\n\n")
        mk.write("".join(appendix))

if __name__ == '__main__':
    markdown_file = sys.argv[1]
    print(markdown_file)
    md_2_img(markdown_file)
