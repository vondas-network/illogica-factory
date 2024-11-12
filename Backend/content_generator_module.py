import cohere
import json
import random
import time
import nltk
from nltk.corpus import words

# Download the word list (only needs to be run once)
nltk.download('words')

class ContentGenerator:
    def __init__(self, api_key):
        self.cohere_client = cohere.Client(api_key)

    def generate_random_words(self, num_words=25):
        """Generate a list of random words."""
        word_list = words.words()
        return random.sample(word_list, num_words)

    def generate_prompt(self, seeds, num_sentences=6, max_tokens=200):
        """Generate a descriptive paragraph using the seed words."""
        prompt = f"Generate an artistic, yet intelligent with a way of educating people on new dimensions and unique paragraph suitable for a video, viral narrative, coehsive and factual, using these words: {', '.join(seeds)}. The paragraph should contain {num_sentences} complete sentences."
        
        response = self.cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.8
        )
        
        return response.generations[0].text.strip()

    def generate_title(self, description, iteration, max_tokens=50):
        """Generate a title for the provided description."""
        title_prompts = [
            f"Create a captivating title that reflects the essence of this description:\n\nDescription: {description}\n\nTitle:",
            f"What's a catchy, viral title for this description that sparks interest?\n\nDescription: {description}\n\nTitle:",
            f"Generate an engaging and unique title based on this description:\n\nDescription: {description}\n\nTitle:",
            f"Think of a creative title that could make this description go viral:\n\nDescription: {description}\n\nTitle:",
            f"Provide a powerful title for the following description that grabs attention:\n\nDescription: {description}\n\nTitle:"
        ]
        
        prompt = title_prompts[iteration % len(title_prompts)]
        
        response = self.cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.9
        )
        
        return response.generations[0].text.strip()

    def generate_new_seeds(self, prompt, num_seeds=5):
        """Generate new seed words based on the generated description."""
        words_from_prompt = prompt.split()
        new_seeds_from_prompt = random.sample(words_from_prompt, min(num_seeds, len(words_from_prompt)))
        random_words = self.generate_random_words(num_seeds)
        mixed_seeds = random.sample(new_seeds_from_prompt + random_words, num_seeds)
        
        return mixed_seeds

    def process_prompts(self, initial_seeds, iterations, num_sentences):
        """Generate multiple iterations of prompts and titles."""
        seeds = initial_seeds
        results = []

        for i in range(iterations):
            prompt = self.generate_prompt(seeds, num_sentences=num_sentences)
            title = self.generate_title(prompt, i)
            new_seeds = self.generate_new_seeds(prompt)

            results.append({
                "iteration": i + 1,
                "title": title,
                "description": prompt,
                "seed_words": new_seeds
            })

            seeds = new_seeds
            time.sleep(1)  # Delay to avoid too many API calls in a short time

        return results

    def export_to_json(self, data, filename=None):
        """Export the generated content to a JSON file."""
        if not filename:
            timestamp = int(time.time())  # Generate Linux timestamp
            filename = f"generated_content_{timestamp}.json"  # Append timestamp to filename
        
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"\nData exported to {filename}")

# Example usage inside another program:
# from content_generator_module import ContentGenerator
# generator = ContentGenerator('1A71k81JllQrIjzKB766jHO7umJBEY7m7lDFYWlt')
# initial_seeds = generator.generate_random_words(25)
# results = generator.process_prompts(initial_seeds, iterations=1, num_sentences=3)
# generator.export_to_json(results)
