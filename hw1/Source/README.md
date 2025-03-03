# data-visualization


### English Vocabulary Learning Application

#### **Overview**

This application helps users improve their English vocabulary through interactive learning modes, including listening, phonetic practice, and meaning recall. It combines auditory and visual cues to create an engaging and effective learning experience.

#### **Features**

**Multimodal Learning Approach**

The application offers three learning strategies:

* **Listening to English**
  * Plays English words for users to identify their meanings.
  * Enhances listening and comprehension skills.
* **Listening to Vietnamese**
  * Plays Vietnamese meanings for users to guess the corresponding English words.
  * Strengthens translation and vocabulary recall.
* **Phonetic Practice**
  * Displays phonetic transcriptions of words for pronunciation practice.
  * Encourages accurate spoken English.

#### **System Benefits**

* **Engaging Modes** : Provides multiple learning approaches to keep users motivated.
* **Personalization** : Offers instant feedback on answers, helping users identify areas for improvement.
* **Scalable Design** : Easily integrates new vocabulary for extended learning.
* **Interactive Feedback** : Encourages active participation and tracks user progress.

#### **Technical Implementation**

**Data Handling**

* Predefined vocabulary list with English words, phonetics, and Vietnamese meanings.
* Dynamic shuffling of vocabulary to ensure varied learning sessions.

**Functionalities**

* **Audio Playback** : Utilizes `gTTS` and `playsound` to provide audio support for words and meanings.
* **Answer Validation** : Compares user inputs with correct answers, supporting case-insensitive and accent-independent matching.
* **Session Management** : Tracks learned words and offers the option to restart or continue learning.

#### **Getting Started**

**Prerequisites**

* Python 3.8+
* Required libraries: `tkinter`, `gTTS`, `playsound`, `unidecode`

**Installation**

1. Install Python and required dependencies.
2. Run the application script using:
   ```bash
   python your_script_name.py  
   ```

**Future Improvements**

* Adding more vocabulary sets and custom import options.
* Introducing gamified elements like quizzes and rewards.
* Supporting progress tracking and saving for users.
