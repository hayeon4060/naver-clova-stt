import argparse
import io
import json

def parsing(filepath):

    fileToWrite = open(filepath[0:-4]+"txt", "w")

    with open(filepath, 'rt', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        i =1
        for alts in data['response']['results']:
            fileToWrite.write(str(i) + " : ")
            fileToWrite.write(str(alts['alternatives'][0]['transcript']))
            fileToWrite.write("\n")
            i +=1
    fileToWrite.close()

if __name__ =='__main__':
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File of GCS path for audio file to be recognized')
    args = parser.parse_args()
    parsing(args.path)