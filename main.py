import os
import json
from webdriver import fillOutForm

def main():

    artifactList = os.listdir('../artifact-auto-capture/artifactsAnnotations/')

    for i in range(len(artifactList)):
    
        with open(os.path.join('../artifact-auto-capture/artifactsAnnotations', artifactList[i])) as f:
            artifactInfo = json.load(f)

        print(artifactInfo)

        fillOutForm(artifactInfo['name'], artifactInfo['type'], artifactInfo['level'], artifactInfo['main'], artifactInfo['sub'])

if __name__ == '__main__':
    main()