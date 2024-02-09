{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "14M41bEliuVfxuTZlin5__TnR5pToawQv",
      "authorship_tag": "ABX9TyMKZpzf5MEPcuik1EPohEPs",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dhananjay23033/CSE508_Winter2024_A1_MT23033/blob/main/CSE508_Winter2024_A1_MT23033.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Q1 Data Preprocessing**"
      ],
      "metadata": {
        "id": "VwTrJzgd80D8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **a. Lowercase the Text**"
      ],
      "metadata": {
        "id": "hP8lTeWE_lry"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uOBjaMaH2pq_",
        "outputId": "57a6c144-3521-498d-c50f-bcb4f2e97df7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of file /content/drive/MyDrive/Colab Notebooks/text_files/file890.txt:\n",
            "My 3rd Joyo Pedal, I'm falling in love with that company, solid great sounding pedals for a fraction of other brands.\n",
            "Be advised, the effect of this pedal is very subtle... I use it with my mustang V, which already models other amps, this pedal just makes it sound way more realistic and adds some dynamics to your playing.\n",
            " Totally worth it for anybody that wants to improve their tone... You have to have a good ear though.\n",
            "I've read some reviews of people hooking this pedal before their amp input... since this pedal has it's own pre amp, this way of hooking it up will produce some noise.\n",
            " Connect it to your FX send return.\n",
            "I also own the American sound .... both great... depending on my mood I play them both equally... You just can't go wrong with Joyo\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file890.txt:\n",
            "my 3rd joyo pedal, i'm falling in love with that company, solid great sounding pedals for a fraction of other brands.\n",
            "be advised, the effect of this pedal is very subtle... i use it with my mustang v, which already models other amps, this pedal just makes it sound way more realistic and adds some dynamics to your playing.\n",
            " totally worth it for anybody that wants to improve their tone... you have to have a good ear though.\n",
            "i've read some reviews of people hooking this pedal before their amp input... since this pedal has it's own pre amp, this way of hooking it up will produce some noise.\n",
            " connect it to your fx send return.\n",
            "i also own the american sound .... both great... depending on my mood i play them both equally... you just can't go wrong with joyo\n",
            "\n",
            "Contents of file /content/drive/MyDrive/Colab Notebooks/text_files/file225.txt:\n",
            "The cover is very beautiful, mainly the interior. One con I find is that it is too heavy and uncomfortable to transport.\n",
            "The main reason why I rate it with 1 stars is that the first week of use (very careful) one of the hinges broke. I can not find another explanation than poor product quality\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file225.txt:\n",
            "the cover is very beautiful, mainly the interior. one con i find is that it is too heavy and uncomfortable to transport.\n",
            "the main reason why i rate it with 1 stars is that the first week of use (very careful) one of the hinges broke. i can not find another explanation than poor product quality\n",
            "\n",
            "Contents of file /content/drive/MyDrive/Colab Notebooks/text_files/file903.txt:\n",
            "This guitar is perfect in every way! It's so easy to play and sounds fantastic! Perfectly balanced with zero neck dive. The bomb inlays just look cool! I definitely plan on buying more Hardluck Kings guitars!\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file903.txt:\n",
            "this guitar is perfect in every way! it's so easy to play and sounds fantastic! perfectly balanced with zero neck dive. the bomb inlays just look cool! i definitely plan on buying more hardluck kings guitars!\n",
            "\n",
            "Contents of file /content/drive/MyDrive/Colab Notebooks/text_files/file902.txt:\n",
            "Beautiful, well-made strap. Matches my guitar nicely. Perfect.\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file902.txt:\n",
            "beautiful, well-made strap. matches my guitar nicely. perfect.\n",
            "\n",
            "Contents of file /content/drive/MyDrive/Colab Notebooks/text_files/file199.txt:\n",
            "Amazing and highly different Wah from ibanez,This is the WAH YA WANT!!,too many reasons!,Just check it out!!!\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file199.txt:\n",
            "amazing and highly different wah from ibanez,this is the wah ya want!!,too many reasons!,just check it out!!!\n",
            "\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "\n",
        "# Function to lowercase the text of a file and save it\n",
        "def lowercase_file(file_path, output_path):\n",
        "    with open(file_path, 'r') as f:\n",
        "        text = f.read().lower()\n",
        "\n",
        "    with open(output_path, 'w') as f:\n",
        "        f.write(text)\n",
        "\n",
        "# Function to print the contents of a file\n",
        "def print_file_contents(file_path):\n",
        "    with open(file_path, 'r') as f:\n",
        "        contents = f.read()\n",
        "        print(f\"Contents of file {file_path}:\\n{contents}\\n\")\n",
        "\n",
        "# Folder paths\n",
        "input_folder = '/content/drive/MyDrive/Colab Notebooks/text_files'\n",
        "output_folder = '/content/preprocessed_text_files/lowercase'\n",
        "\n",
        "# Ensure the output folder exists, create it if necessary\n",
        "os.makedirs(output_folder, exist_ok=True)\n",
        "\n",
        "# Get a list of all files in the input folder\n",
        "files = os.listdir(input_folder)\n",
        "\n",
        "# counter to track the no of printed files\n",
        "count=0\n",
        "\n",
        "for file_name in files:\n",
        "    input_file_path = os.path.join(input_folder, file_name)\n",
        "    output_file_path = os.path.join(output_folder, file_name)\n",
        "\n",
        "    # Lowercase the text and save the file\n",
        "    lowercase_file(input_file_path, output_file_path)\n",
        "\n",
        "    if(count<5):\n",
        "      # Print contents of the original and lowercase files\n",
        "      print_file_contents(input_file_path)\n",
        "      print_file_contents(output_file_path)\n",
        "      count+=1"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **b. Perform Tokenization**"
      ],
      "metadata": {
        "id": "tFlCOWliAQ_z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import nltk\n",
        "from nltk.tokenize import word_tokenize\n",
        "\n",
        "# Download the punkt tokenizer if not already downloaded\n",
        "nltk.download('punkt')\n",
        "\n",
        "# Function to tokenize the text of a file and save it\n",
        "def tokenize_file(file_path, output_path):\n",
        "    with open(file_path, 'r') as f:\n",
        "        text = f.read()\n",
        "        tokens = word_tokenize(text)\n",
        "\n",
        "    with open(output_path, 'w') as f:\n",
        "        f.write(\" \".join(tokens))\n",
        "\n",
        "# Folder paths\n",
        "input_folder = '/content/preprocessed_text_files/lowercase'\n",
        "output_folder = '/content/preprocessed_text_files/tokenized'\n",
        "\n",
        "# Ensure the output folder exists, create it if necessary\n",
        "os.makedirs(output_folder, exist_ok=True)\n",
        "\n",
        "# Get a list of all files in the input folder\n",
        "files = os.listdir(input_folder)\n",
        "\n",
        "# counter to track the no of printed files\n",
        "count=0\n",
        "\n",
        "# Process all files in the input folder\n",
        "for file_name in files:\n",
        "    input_file_path = os.path.join(input_folder, file_name)\n",
        "    output_file_path = os.path.join(output_folder, file_name)\n",
        "\n",
        "    # Tokenize the text and save the file\n",
        "    tokenize_file(input_file_path, output_file_path)\n",
        "\n",
        "    # Print contents of the 5 original and processed files\n",
        "    if(count<5):\n",
        "      print_file_contents(input_file_path)\n",
        "      print_file_contents(output_file_path)\n",
        "      count+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "np0CFvLgBgCA",
        "outputId": "28eaf28b-9537-4df4-f2c7-8104aa955863"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt.zip.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of file /content/preprocessed_text_files/lowercase/file571.txt:\n",
            "i have a garage sale piece of junk mij hollowbody that i've used amazon to build for cheap.  it's been a blast and this fit the bill perfectly.\n",
            "\n",
            "i cannot tell you how surprised i am at how good this sounds with this guitar.  it has inspired me to play open tuning slide because the tone through a simple boss distortion pedal is so cool.\n",
            "\n",
            "i would absolutely purchase this again for another cheapo build!\n",
            "\n",
            "if you're looking at this, buy it.  don't think twice.\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file571.txt:\n",
            "i have a garage sale piece of junk mij hollowbody that i 've used amazon to build for cheap . it 's been a blast and this fit the bill perfectly . i can not tell you how surprised i am at how good this sounds with this guitar . it has inspired me to play open tuning slide because the tone through a simple boss distortion pedal is so cool . i would absolutely purchase this again for another cheapo build ! if you 're looking at this , buy it . do n't think twice .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file144.txt:\n",
            "cool little portable sound amplifier, for when you just got to make noise without waking the neighborhood! very light, hope it's impact resistant so i can stuff it in a back pack with other goodies. i'm using it for harmonica, slide guitar, or as a powered speaker for my media players. the sound is decent and the battery seem to last long enough. i am happy with this purchase. way to go danelectro!\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file144.txt:\n",
            "cool little portable sound amplifier , for when you just got to make noise without waking the neighborhood ! very light , hope it 's impact resistant so i can stuff it in a back pack with other goodies . i 'm using it for harmonica , slide guitar , or as a powered speaker for my media players . the sound is decent and the battery seem to last long enough . i am happy with this purchase . way to go danelectro !\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file356.txt:\n",
            "works way better than i thought. turned an old, untouched 12 string into a respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file356.txt:\n",
            "works way better than i thought . turned an old , untouched 12 string into a respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file846.txt:\n",
            "i needed a smaller pedalboard for my solo setup and considered building one. when i saw the price on this one i decided to try it. awesome. i fit a large amp pedal, eq pedal, loop pedal, loop controller pedal and surge protector on this bad boy with room to spare. well made and packs up compactly. before you break out the plywood and velcro give this pedalboard a go.\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file846.txt:\n",
            "i needed a smaller pedalboard for my solo setup and considered building one . when i saw the price on this one i decided to try it . awesome . i fit a large amp pedal , eq pedal , loop pedal , loop controller pedal and surge protector on this bad boy with room to spare . well made and packs up compactly . before you break out the plywood and velcro give this pedalboard a go .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/lowercase/file343.txt:\n",
            "upgrading from a numark mixtrack pro to this is night and day.  while i didn't buy it off amazon, i've attached my picture of the set up.  definitely... buy a high quality flight case.  you don't want to haul a $1000 masterpiece and haul this in something that doesn't protect your investment.\n",
            "\n",
            "i'm a hobbyist dj.  i like messing around with different styles while not being dedicated to any one. this controller does it all. it does so much, i honestly think they should have online courses to use the more advanced features.  sure you can run this right out of the box with cross fading and beat matching.  however that's not why you make this sort of investment.  you want to do something someone else can't. to make a sound unique and an audience captivated.  worth... every.. dollar.\n",
            "\n",
            "sound, lights, function, and every bit of it is mona lisa. there are 100's of youtube reviews on this controller.  do your homework. watch them. it's your money and one person alone can't tell you how great this controller is.  you'll know when you experience it.\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file343.txt:\n",
            "upgrading from a numark mixtrack pro to this is night and day . while i did n't buy it off amazon , i 've attached my picture of the set up . definitely ... buy a high quality flight case . you do n't want to haul a $ 1000 masterpiece and haul this in something that does n't protect your investment . i 'm a hobbyist dj . i like messing around with different styles while not being dedicated to any one . this controller does it all . it does so much , i honestly think they should have online courses to use the more advanced features . sure you can run this right out of the box with cross fading and beat matching . however that 's not why you make this sort of investment . you want to do something someone else ca n't . to make a sound unique and an audience captivated . worth ... every .. dollar . sound , lights , function , and every bit of it is mona lisa . there are 100 's of youtube reviews on this controller . do your homework . watch them . it 's your money and one person alone ca n't tell you how great this controller is . you 'll know when you experience it .\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **c. Remove Stopwords**"
      ],
      "metadata": {
        "id": "RbskpYCNEgFe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import nltk\n",
        "from nltk.corpus import stopwords\n",
        "\n",
        "# Download the stopwords if not already downloaded\n",
        "nltk.download('stopwords')\n",
        "\n",
        "# Function to remove stopwords from a list of tokens and save it\n",
        "def remove_stopwords(tokens):\n",
        "    filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]\n",
        "    return filtered_tokens\n",
        "\n",
        "# Folder paths\n",
        "input_folder = '/content/preprocessed_text_files/tokenized'\n",
        "output_folder = '/content/preprocessed_text_files/without_stopwords'\n",
        "\n",
        "# Ensure the output folder exists, create it if necessary\n",
        "os.makedirs(output_folder, exist_ok=True)\n",
        "\n",
        "# Get a list of all files in the input folder\n",
        "files = os.listdir(input_folder)\n",
        "\n",
        "# counter to track no of printed files\n",
        "count=0\n",
        "\n",
        "# Process all files in the input folder\n",
        "for file_name in files:\n",
        "    input_file_path = os.path.join(input_folder, file_name)\n",
        "    output_file_path = os.path.join(output_folder, file_name)\n",
        "\n",
        "    # Read the tokenized text from the file\n",
        "    with open(input_file_path, 'r') as f:\n",
        "        tokens = nltk.word_tokenize(f.read())\n",
        "\n",
        "    # Remove stopwords from the list of tokens and save the file\n",
        "    tokens = remove_stopwords(tokens)\n",
        "\n",
        "    with open(output_file_path, 'w') as f:\n",
        "        f.write(\" \".join(tokens))\n",
        "\n",
        "    # Print contents of the 5 original and processed files\n",
        "    if(count<5):\n",
        "     print_file_contents(input_file_path)\n",
        "     print_file_contents(output_file_path)\n",
        "     count+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cDSqzuGCEbBh",
        "outputId": "aad32aed-2aa0-4769-cf6f-5b4013915c81"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of file /content/preprocessed_text_files/tokenized/file571.txt:\n",
            "i have a garage sale piece of junk mij hollowbody that i 've used amazon to build for cheap . it 's been a blast and this fit the bill perfectly . i can not tell you how surprised i am at how good this sounds with this guitar . it has inspired me to play open tuning slide because the tone through a simple boss distortion pedal is so cool . i would absolutely purchase this again for another cheapo build ! if you 're looking at this , buy it . do n't think twice .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file571.txt:\n",
            "garage sale piece junk mij hollowbody 've used amazon build cheap . 's blast fit bill perfectly . tell surprised good sounds guitar . inspired play open tuning slide tone simple boss distortion pedal cool . would absolutely purchase another cheapo build ! 're looking , buy . n't think twice .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file144.txt:\n",
            "cool little portable sound amplifier , for when you just got to make noise without waking the neighborhood ! very light , hope it 's impact resistant so i can stuff it in a back pack with other goodies . i 'm using it for harmonica , slide guitar , or as a powered speaker for my media players . the sound is decent and the battery seem to last long enough . i am happy with this purchase . way to go danelectro !\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file144.txt:\n",
            "cool little portable sound amplifier , got make noise without waking neighborhood ! light , hope 's impact resistant stuff back pack goodies . 'm using harmonica , slide guitar , powered speaker media players . sound decent battery seem last long enough . happy purchase . way go danelectro !\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file356.txt:\n",
            "works way better than i thought . turned an old , untouched 12 string into a respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file356.txt:\n",
            "works way better thought . turned old , untouched 12 string respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file846.txt:\n",
            "i needed a smaller pedalboard for my solo setup and considered building one . when i saw the price on this one i decided to try it . awesome . i fit a large amp pedal , eq pedal , loop pedal , loop controller pedal and surge protector on this bad boy with room to spare . well made and packs up compactly . before you break out the plywood and velcro give this pedalboard a go .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file846.txt:\n",
            "needed smaller pedalboard solo setup considered building one . saw price one decided try . awesome . fit large amp pedal , eq pedal , loop pedal , loop controller pedal surge protector bad boy room spare . well made packs compactly . break plywood velcro give pedalboard go .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/tokenized/file343.txt:\n",
            "upgrading from a numark mixtrack pro to this is night and day . while i did n't buy it off amazon , i 've attached my picture of the set up . definitely ... buy a high quality flight case . you do n't want to haul a $ 1000 masterpiece and haul this in something that does n't protect your investment . i 'm a hobbyist dj . i like messing around with different styles while not being dedicated to any one . this controller does it all . it does so much , i honestly think they should have online courses to use the more advanced features . sure you can run this right out of the box with cross fading and beat matching . however that 's not why you make this sort of investment . you want to do something someone else ca n't . to make a sound unique and an audience captivated . worth ... every .. dollar . sound , lights , function , and every bit of it is mona lisa . there are 100 's of youtube reviews on this controller . do your homework . watch them . it 's your money and one person alone ca n't tell you how great this controller is . you 'll know when you experience it .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file343.txt:\n",
            "upgrading numark mixtrack pro night day . n't buy amazon , 've attached picture set . definitely ... buy high quality flight case . n't want haul $ 1000 masterpiece haul something n't protect investment . 'm hobbyist dj . like messing around different styles dedicated one . controller . much , honestly think online courses use advanced features . sure run right box cross fading beat matching . however 's make sort investment . want something someone else ca n't . make sound unique audience captivated . worth ... every .. dollar . sound , lights , function , every bit mona lisa . 100 's youtube reviews controller . homework . watch . 's money one person alone ca n't tell great controller . 'll know experience .\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **d. Remove Punctuations**"
      ],
      "metadata": {
        "id": "4VhJhggQGwcD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import string\n",
        "import nltk\n",
        "from nltk.corpus import stopwords\n",
        "\n",
        "# Download the stopwords if not already downloaded\n",
        "nltk.download('stopwords')\n",
        "\n",
        "# Function to remove punctuation from a string\n",
        "def remove_punctuation(text):\n",
        "    return text.translate(str.maketrans('', '', string.punctuation))\n",
        "\n",
        "# Folder paths\n",
        "input_folder = '/content/preprocessed_text_files/without_stopwords'\n",
        "output_folder = '/content/preprocessed_text_files/without_punctuations'\n",
        "\n",
        "# Ensure the output folder exists, create it if necessary\n",
        "os.makedirs(output_folder, exist_ok=True)\n",
        "\n",
        "# Get a list of all files in the input folder\n",
        "files = os.listdir(input_folder)\n",
        "\n",
        "# counter to track no of printed files\n",
        "count=0\n",
        "\n",
        "# Process all files in the input folder\n",
        "for file_name in files:\n",
        "    input_file_path = os.path.join(input_folder, file_name)\n",
        "    output_file_path = os.path.join(output_folder, file_name)\n",
        "\n",
        "    # Read the text from the file\n",
        "    with open(input_file_path, 'r') as f:\n",
        "        text = f.read()\n",
        "\n",
        "    # Remove punctuation from the text and save the file\n",
        "    cleaned_text = remove_punctuation(text)\n",
        "    with open(output_file_path, 'w') as f:\n",
        "        f.write(cleaned_text)\n",
        "\n",
        "    # Print contents of the 5 original and processed files\n",
        "    if(count<5):\n",
        "     print_file_contents(input_file_path)\n",
        "     print_file_contents(output_file_path)\n",
        "     count+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cofDP7OFG3kI",
        "outputId": "365df297-01d8-4329-818a-90f6339aa8aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of file /content/preprocessed_text_files/without_stopwords/file571.txt:\n",
            "garage sale piece junk mij hollowbody 've used amazon build cheap . 's blast fit bill perfectly . tell surprised good sounds guitar . inspired play open tuning slide tone simple boss distortion pedal cool . would absolutely purchase another cheapo build ! 're looking , buy . n't think twice .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file571.txt:\n",
            "garage sale piece junk mij hollowbody ve used amazon build cheap  s blast fit bill perfectly  tell surprised good sounds guitar  inspired play open tuning slide tone simple boss distortion pedal cool  would absolutely purchase another cheapo build  re looking  buy  nt think twice \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file144.txt:\n",
            "cool little portable sound amplifier , got make noise without waking neighborhood ! light , hope 's impact resistant stuff back pack goodies . 'm using harmonica , slide guitar , powered speaker media players . sound decent battery seem last long enough . happy purchase . way go danelectro !\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file144.txt:\n",
            "cool little portable sound amplifier  got make noise without waking neighborhood  light  hope s impact resistant stuff back pack goodies  m using harmonica  slide guitar  powered speaker media players  sound decent battery seem last long enough  happy purchase  way go danelectro \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file356.txt:\n",
            "works way better thought . turned old , untouched 12 string respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file356.txt:\n",
            "works way better thought  turned old  untouched 12 string respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file846.txt:\n",
            "needed smaller pedalboard solo setup considered building one . saw price one decided try . awesome . fit large amp pedal , eq pedal , loop pedal , loop controller pedal surge protector bad boy room spare . well made packs compactly . break plywood velcro give pedalboard go .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file846.txt:\n",
            "needed smaller pedalboard solo setup considered building one  saw price one decided try  awesome  fit large amp pedal  eq pedal  loop pedal  loop controller pedal surge protector bad boy room spare  well made packs compactly  break plywood velcro give pedalboard go \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_stopwords/file343.txt:\n",
            "upgrading numark mixtrack pro night day . n't buy amazon , 've attached picture set . definitely ... buy high quality flight case . n't want haul $ 1000 masterpiece haul something n't protect investment . 'm hobbyist dj . like messing around different styles dedicated one . controller . much , honestly think online courses use advanced features . sure run right box cross fading beat matching . however 's make sort investment . want something someone else ca n't . make sound unique audience captivated . worth ... every .. dollar . sound , lights , function , every bit mona lisa . 100 's youtube reviews controller . homework . watch . 's money one person alone ca n't tell great controller . 'll know experience .\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file343.txt:\n",
            "upgrading numark mixtrack pro night day  nt buy amazon  ve attached picture set  definitely  buy high quality flight case  nt want haul  1000 masterpiece haul something nt protect investment  m hobbyist dj  like messing around different styles dedicated one  controller  much  honestly think online courses use advanced features  sure run right box cross fading beat matching  however s make sort investment  want something someone else ca nt  make sound unique audience captivated  worth  every  dollar  sound  lights  function  every bit mona lisa  100 s youtube reviews controller  homework  watch  s money one person alone ca nt tell great controller  ll know experience \n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Package stopwords is already up-to-date!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **e. Remove blank space tokens**"
      ],
      "metadata": {
        "id": "GIUZ1dcDJHV5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import string\n",
        "import nltk\n",
        "\n",
        "# Function to remove blank space tokens from a list of tokens\n",
        "def remove_blank_space(tokens):\n",
        "    return [token.strip() for token in tokens if token.strip()]\n",
        "\n",
        "# Folder paths\n",
        "input_folder = '/content/preprocessed_text_files/without_punctuations'\n",
        "output_folder = '/content/preprocessed_text_files/final_cleaned'\n",
        "\n",
        "# Ensure the output folder exists, create it if necessary\n",
        "os.makedirs(output_folder, exist_ok=True)\n",
        "\n",
        "# Get a list of all files in the input folder\n",
        "files = os.listdir(input_folder)\n",
        "\n",
        "# counter to track no of printed files\n",
        "count=0\n",
        "\n",
        "# Process all files in the input folder\n",
        "for file_name in files:\n",
        "    input_file_path = os.path.join(input_folder, file_name)\n",
        "    output_file_path = os.path.join(output_folder, file_name)\n",
        "\n",
        "    # Read the text from the file\n",
        "    with open(input_file_path, 'r') as f:\n",
        "        text = f.read()\n",
        "\n",
        "    # Tokenize the cleaned text\n",
        "    tokens = nltk.word_tokenize(text)\n",
        "\n",
        "    # Remove blank space tokens from the list of tokens\n",
        "    cleaned_tokens = remove_blank_space(tokens)\n",
        "\n",
        "    # Save the final cleaned file\n",
        "    with open(output_file_path, 'w') as f:\n",
        "        f.write(\" \".join(cleaned_tokens))\n",
        "\n",
        "    # Print contents of the 5 original and processed files\n",
        "    if(count<5):\n",
        "     print_file_contents(input_file_path)\n",
        "     print_file_contents(output_file_path)\n",
        "     count+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HzBb7QBIJOcD",
        "outputId": "c487158a-1b3f-413c-c4cd-0ccc19bb310e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of file /content/preprocessed_text_files/without_punctuations/file571.txt:\n",
            "garage sale piece junk mij hollowbody ve used amazon build cheap  s blast fit bill perfectly  tell surprised good sounds guitar  inspired play open tuning slide tone simple boss distortion pedal cool  would absolutely purchase another cheapo build  re looking  buy  nt think twice \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/final_cleaned/file571.txt:\n",
            "garage sale piece junk mij hollowbody ve used amazon build cheap s blast fit bill perfectly tell surprised good sounds guitar inspired play open tuning slide tone simple boss distortion pedal cool would absolutely purchase another cheapo build re looking buy nt think twice\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file144.txt:\n",
            "cool little portable sound amplifier  got make noise without waking neighborhood  light  hope s impact resistant stuff back pack goodies  m using harmonica  slide guitar  powered speaker media players  sound decent battery seem last long enough  happy purchase  way go danelectro \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/final_cleaned/file144.txt:\n",
            "cool little portable sound amplifier got make noise without waking neighborhood light hope s impact resistant stuff back pack goodies m using harmonica slide guitar powered speaker media players sound decent battery seem last long enough happy purchase way go danelectro\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file356.txt:\n",
            "works way better thought  turned old  untouched 12 string respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/final_cleaned/file356.txt:\n",
            "works way better thought turned old untouched 12 string respectable lap guitar\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file846.txt:\n",
            "needed smaller pedalboard solo setup considered building one  saw price one decided try  awesome  fit large amp pedal  eq pedal  loop pedal  loop controller pedal surge protector bad boy room spare  well made packs compactly  break plywood velcro give pedalboard go \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/final_cleaned/file846.txt:\n",
            "needed smaller pedalboard solo setup considered building one saw price one decided try awesome fit large amp pedal eq pedal loop pedal loop controller pedal surge protector bad boy room spare well made packs compactly break plywood velcro give pedalboard go\n",
            "\n",
            "Contents of file /content/preprocessed_text_files/without_punctuations/file343.txt:\n",
            "upgrading numark mixtrack pro night day  nt buy amazon  ve attached picture set  definitely  buy high quality flight case  nt want haul  1000 masterpiece haul something nt protect investment  m hobbyist dj  like messing around different styles dedicated one  controller  much  honestly think online courses use advanced features  sure run right box cross fading beat matching  however s make sort investment  want something someone else ca nt  make sound unique audience captivated  worth  every  dollar  sound  lights  function  every bit mona lisa  100 s youtube reviews controller  homework  watch  s money one person alone ca nt tell great controller  ll know experience \n",
            "\n",
            "Contents of file /content/preprocessed_text_files/final_cleaned/file343.txt:\n",
            "upgrading numark mixtrack pro night day nt buy amazon ve attached picture set definitely buy high quality flight case nt want haul 1000 masterpiece haul something nt protect investment m hobbyist dj like messing around different styles dedicated one controller much honestly think online courses use advanced features sure run right box cross fading beat matching however s make sort investment want something someone else ca nt make sound unique audience captivated worth every dollar sound lights function every bit mona lisa 100 s youtube reviews controller homework watch s money one person alone ca nt tell great controller ll know experience\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Q2. Unigram Inverted Index and Boolean Queries**"
      ],
      "metadata": {
        "id": "osagBEVd_jSZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **a. Unigram Index Construction**"
      ],
      "metadata": {
        "id": "2_80py5DFuJO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "\n",
        "# Function to read all files in a directory and return a list of file paths\n",
        "def get_file_paths(directory):\n",
        "    file_paths = []\n",
        "    for root, _, files in os.walk(directory):\n",
        "        for file in files:\n",
        "            file_paths.append(os.path.join(root, file))\n",
        "    return file_paths\n",
        "\n",
        "# Function to tokenize text\n",
        "def tokenize(text):\n",
        "    return text.split()\n",
        "\n",
        "# Function to extract document ID from file name\n",
        "def extract_doc_id(file_path):\n",
        "    file_name = os.path.basename(file_path)\n",
        "    return int(file_name.split('.')[0].split('file')[1])\n",
        "\n",
        "# Function to create a unigram inverted index\n",
        "def create_inverted_index(file_paths):\n",
        "    inverted_index = {}\n",
        "    for file_path in file_paths:\n",
        "        doc_id = extract_doc_id(file_path)\n",
        "        with open(file_path, 'r') as file:\n",
        "            text = file.read()\n",
        "            tokens = tokenize(text)\n",
        "            for token in tokens:\n",
        "                if token not in inverted_index:\n",
        "                    inverted_index[token] = set()\n",
        "                inverted_index[token].add(doc_id)\n",
        "    return inverted_index\n",
        "\n",
        "# Path to the directory containing the preprocessed files\n",
        "preprocessed_folder = '/content/preprocessed_text_files/final_cleaned'\n",
        "\n",
        "# Get file paths\n",
        "file_paths = get_file_paths(preprocessed_folder)\n",
        "\n",
        "# Create the inverted index\n",
        "unigram_inverted_index = create_inverted_index(file_paths)\n",
        "\n",
        "# Save the inverted index using pickle\n",
        "with open('unigram_inverted_index.pickle', 'wb') as f:\n",
        "    pickle.dump(unigram_inverted_index, f)"
      ],
      "metadata": {
        "id": "DHieIbHv_7K-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Query Support**"
      ],
      "metadata": {
        "id": "jYmhlSNGGCPE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Function to perform AND operation\n",
        "def perform_and(term1_docs, term2_docs):\n",
        "    return term1_docs.intersection(term2_docs)\n",
        "\n",
        "# Function to perform OR operation\n",
        "def perform_or(term1_docs, term2_docs):\n",
        "    return term1_docs.union(term2_docs)\n",
        "\n",
        "# Function to perform AND NOT operation\n",
        "def perform_and_not(term1_docs, term2_docs):\n",
        "    return term1_docs.difference(term2_docs)\n",
        "\n",
        "# Function to perform OR NOT operation\n",
        "def perform_or_not(term1_docs, term2_docs, all_docs):\n",
        "    return all_docs.difference(term2_docs).union(term1_docs)\n",
        "\n",
        "# Function to perform query operation\n",
        "def perform_query(inverted_index, query):\n",
        "    result = inverted_index[query.terms[0]]\n",
        "    all_docs = set(range(1, 1000))\n",
        "    for term, operator in zip(query.terms[1:], query.operators):\n",
        "        set2 = inverted_index[term] if term in inverted_index else set()\n",
        "        # print(f\"{result} {operator} {set2} = \", end=' ')\n",
        "        if operator == 'AND':\n",
        "            result = perform_and(result, set2)\n",
        "        elif operator == 'OR':\n",
        "            result = perform_or(result, set2)\n",
        "        elif operator == 'AND NOT':\n",
        "            result = perform_and_not(result, set2)\n",
        "        elif operator == 'OR NOT':\n",
        "            result = perform_or_not(result, set2, all_docs)\n",
        "        # print(result)\n",
        "    return result\n",
        "\n",
        "# Function to print the results of a query\n",
        "def print_query_results(query_num, result_docs):\n",
        "    print(f\"Query {query_num}:\")\n",
        "    print(f\"Number of documents retrieved for query {query_num}: {len(result_docs)}\")\n",
        "    print(f\"Names of the documents retrieved for query {query_num}: {', '.join(['file' + str(doc) + '.txt' for doc in sorted(result_docs)])}\")\n",
        "\n",
        "# Load the inverted index from the pickle file\n",
        "with open('unigram_inverted_index.pickle', 'rb') as f:\n",
        "    loaded_inverted_index = pickle.load(f)\n",
        "\n",
        "# object to store queries\n",
        "class Query:\n",
        "    def __init__(this, text, operations):\n",
        "      this.terms = preprocess(text)\n",
        "      this.operators = remove_blank_space(operations.upper().split(','))\n",
        "\n",
        "# perform prepocessing like lowering case, removing stopwords, punctuations, on the text\n",
        "def preprocess(text):\n",
        "    tokens = remove_blank_space(remove_stopwords(remove_punctuation(text.lower()).split()))\n",
        "    return tokens\n",
        "\n",
        "# list of queries\n",
        "queries = []\n",
        "\n",
        "# take user input\n",
        "N = int(input())\n",
        "for i in range(N):\n",
        "    queries.append(Query(input(),input()))\n",
        "\n",
        "# # process each query\n",
        "for i, query in enumerate(queries, start=1):\n",
        "    print_query_results(i, perform_query(loaded_inverted_index, query))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R-taxw0kEjiA",
        "outputId": "3ee3c0af-2ad9-4b92-880d-5e1ffa1244e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "technique:  {918, 23}\n"
          ]
        }
      ]
    }
  ]
}