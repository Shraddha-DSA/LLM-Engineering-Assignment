# LLM Quantisation Benchmark

Comparison: FP16 vs Q4_K_M


## Prompt 1

**Question:** What is the capital of Australia, and why isn't it Sydney?

### FP16

Speed: 2.56 tokens/sec

The capital of Australia is Canberra. While Sydney is the largest city in Australia and a major cultural and economic center, Canberra has been the country's capital since 1908. The decision to make Canberra the capital was made due to a compromise between the two main cities, Sydney and Melbourne, which were both vying for the position.

In the late 19th century, the Australian government was looking for a new capital city to replace Melbourne, which was the temporary capital at the time. A competition was held to design the new capital, and the winner was Walter Burley Griffin, an American architect. Griffin's design for Canberra was chosen for its unique layout, which featured a central city surrounded by a series of lakes and gardens.

Sydney was a strong contender for the capital, but it was ultimately decided that Canberra's central location and neutral status (not being the largest city) made it a more suitable choice. Canberra was officially opened as the capital in 1927, and it has remained so to this day.

It's worth noting that while Canberra is the capital, Sydney is still the most populous city in Australia and is often referred to as the country's economic and cultural hub.

### Q4

Speed: 6.57 tokens/sec

The capital of Australia is Canberra. While Sydney is the largest city in Australia and a major cultural and economic hub, Canberra has been the country's capital since 1908. The decision to make Canberra the capital was made due to a compromise between the competing claims of Sydney and Melbourne, which were both major cities at the time.

In 1908, the Australian government decided to build a new capital city in the Australian Capital Territory (ACT), which was created specifically for this purpose. The city was designed by American architect Walter Burley Griffin, who won an international design competition for the city in 1912. Canberra was officially opened as the capital of Australia on March 12, 1927.

Sydney, on the other hand, was chosen as the largest city in Australia and the seat of the state government of New South Wales. While Sydney is a major cultural and economic center, Canberra's location in the center of the country makes it a more neutral and accessible location for the federal government.

It's worth noting that while Canberra is the capital, Sydney is still the most populous city in Australia and a major tourist destination.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 2

**Question:** A train leaves at 14:20 and the trip takes 2h 55m. When does it arrive?

### FP16

Speed: 2.55 tokens/sec

To find the arrival time, we need to add the travel time to the departure time.

Departure time: 14:20
Travel time: 2 hours 55 minutes

First, add the 2 hours to the departure time:
14:20 + 2 hours = 16:20

Then, add the remaining 55 minutes to the result:
16:20 + 55 minutes = 17:15

So, the train arrives at 17:15.

### Q4

Speed: 7.39 tokens/sec

To find the arrival time, we need to add the travel time to the departure time.

Departure time: 14:20
Travel time: 2 hours 55 minutes

First, let's convert the travel time to just hours:
2 hours 55 minutes = 2.92 hours (approximately)

Now, let's add the travel time to the departure time:
14:20 + 2 hours 55 minutes = 17:15

So, the train arrives at approximately 17:15.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 3

**Question:** If 5 machines make 5 widgets in 5 minutes, how long do 100 machines take to make 100 widgets?

### FP16

Speed: 2.56 tokens/sec

If 5 machines make 5 widgets in 5 minutes, it means that each machine makes 1 widget in 5 minutes.

If we have 100 machines, it will take each machine 5 minutes to make 1 widget. Therefore, 100 machines will take 5 minutes to make 100 widgets.

So, the answer is 5 minutes.

### Q4

Speed: 6.89 tokens/sec

If 5 machines make 5 widgets in 5 minutes, it means that each machine makes 1 widget in 5 minutes.

If we have 100 machines, each machine will still make 1 widget in 5 minutes. Therefore, 100 machines will also make 100 widgets in 5 minutes.

So, the answer is 5 minutes.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 4

**Question:** Write a Python function that returns the n-th Fibonacci number iteratively.

### FP16

Speed: 2.55 tokens/sec

def fibonacci(n):
    """
    Returns the n-th Fibonacci number iteratively.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # If n is 0, return the first Fibonacci number
    if n == 0:
        return a

    # If n is 1, return the second Fibonacci number
    if n == 1:
        return b

    # Iterate from 2 to n (inclusive) to calculate the n-th Fibonacci number
    for _ in range(2, n + 1):
        # Calculate the next Fibonacci number as the sum of the previous two
        a, b = b, a + b

    # Return the n-th Fibonacci number
    return b

### Q4

Speed: 6.57 tokens/sec

def fibonacci(n):
    """
    Returns the n-th Fibonacci number iteratively.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Iterate from 2 to n (inclusive)
    for _ in range(2, n + 1):
        # Calculate the next Fibonacci number
        a, b = b, a + b

    # Return the n-th Fibonacci number
    return a

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 5

**Question:** Summarise in two sentences: Transformers use self-attention to weigh every token against every other token, letting them model long-range dependencies in parallel, unlike RNNs which process sequentially.

### FP16

Speed: 2.39 tokens/sec

Transformers utilize self-attention mechanisms to weigh every token's importance relative to every other token, enabling the modeling of long-range dependencies in parallel. This approach differs from Recurrent Neural Networks (RNNs), which process information sequentially, allowing Transformers to capture complex relationships between tokens more efficiently.

### Q4

Speed: 6.87 tokens/sec

Transformers use self-attention to weigh every token against every other token, allowing them to model long-range dependencies in parallel. This approach differs from Recurrent Neural Networks (RNNs), which process information sequentially, enabling Transformers to capture complex relationships between tokens in a more efficient and parallelizable manner.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 6

**Question:** Translate to French: 'The meeting has been moved to Thursday afternoon.'

### FP16

Speed: 2.61 tokens/sec

Here's the translation:

"Le rendez-vous a été déplacé à l'après-midi du jeudi."

Here's a breakdown of the translation:

* "The meeting" = "Le rendez-vous"
* "has been moved" = "a été déplacé"
* "to Thursday afternoon" = "à l'après-midi du jeudi"

Note: In French, the word "après-midi" literally means "afternoon", but it's often used to refer to the late afternoon, around 4-6 pm. If you want to be more precise, you could say "à 4 heures de l'après-midi" (at 4 pm) or "à 5 heures de l'après-midi" (at 5 pm).

### Q4

Speed: 7.22 tokens/sec

The translation of "The meeting has been moved to Thursday afternoon" in French is:

"La réunion a été déplacée à l'après-midi du jeudi."

Here's a breakdown of the translation:

* "The meeting" = "La réunion"
* "has been moved" = "a été déplacée"
* "to Thursday afternoon" = "à l'après-midi du jeudi"

Note: In French, the word "après-midi" literally means "afternoon", but it's often used to refer to the late afternoon, around 3-5 pm. If you want to be more precise, you could use "l'après-midi du jeudi" (the afternoon of Thursday) or "à 3 heures du jeudi" (at 3 pm on Thursday).

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 7

**Question:** Write a four-line poem about monsoon rain.

### FP16

Speed: 2.67 tokens/sec

Here is a four-line poem about monsoon rain:

Heavy clouds gather, dark and grey
Monsoon rain comes, washing all away
The scent of wet earth fills the air
Nature's rhythm, beyond compare

### Q4

Speed: 7.06 tokens/sec

Here is a four-line poem about monsoon rain:

Heavy clouds gather in the sky,
Monsoon rain comes pouring by,
Drumming on the roof above,
Nature's rhythm, a soothing love.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 8

**Question:** Explain what a hash table is to a 12-year-old.

### FP16

Speed: 2.58 tokens/sec

Imagine you have a bunch of folders with different labels on them, like "Friends", "School", "Favorite Foods", and so on. Inside each folder, you have a list of things that fit that label, like names of friends, school subjects, or your favorite foods.

A hash table is like a super-efficient way to organize and find things in those folders. Instead of having to look through each folder one by one, you can use a special code to quickly find the folder you need.

Here's how it works:

1. You take a piece of information, like a name or a word, and you turn it into a special code using a secret formula (this is called a "hash function").
2. You use that code to find the corresponding folder (this is called a "bucket").
3. Inside that bucket, you find the list of things that fit the original information.

For example, let's say you want to find all the names of your friends in the "Friends" folder. You would use the hash function to turn the word "Friends" into a code, like "12345". Then, you would look for the bucket labeled "12345" and find the list of names of your friends inside.

Hash tables are really fast and efficient

### Q4

Speed: 6.85 tokens/sec

Imagine you have a bunch of folders, and inside each folder, you have a bunch of notes with different information on them. For example, one folder might have notes about your friends, another folder might have notes about your favorite video games, and another folder might have notes about your favorite sports teams.

A hash table is like a super-organized system that helps you find the notes you need quickly. Instead of having to look through all the folders and notes, you can use a special code to find the notes you want.

Here's how it works:

1. You take the information you want to find (like a friend's name or a video game's title) and turn it into a special code.
2. You use this code to "look up" the folder where the notes are stored.
3. The hash table uses this code to find the correct folder and then finds the note you want.

The really cool thing about hash tables is that they can store a LOT of information, and they can find it really fast. It's like having a super-smart librarian who can find any note you need in just a second!

Hash tables are used in all sorts of things, like computers, phones, and even websites. They help make it easy to store and find

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 9

**Question:** Reply with only valid JSON with keys name (string) and age (int) for a fictional person.

### FP16

Speed: 2.63 tokens/sec

{"name": "John Doe", "age": 30}

### Q4

Speed: 7.12 tokens/sec

{"name": "John Doe", "age": 30}

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---

## Prompt 10

**Question:** Is it ever acceptable to lie? Give a balanced answer in under 100 words.

### FP16

Speed: 2.47 tokens/sec

Lying can be a complex issue, and its acceptability depends on the context and motivations. In some situations, white lies or small deceptions may be told to avoid hurting someone's feelings or maintain social harmony. However, habitual or intentional lying can damage relationships, erode trust, and lead to more severe consequences. It's essential to consider the potential impact on others and one's own integrity. Ultimately, honesty is generally the best policy, and lying should be avoided unless absolutely necessary to prevent harm or protect someone's well-being. Context and intentions play a crucial role in determining acceptability.

### Q4

Speed: 7.09 tokens/sec

Lying can be a complex issue, and its acceptability depends on the context and motivations. In some situations, such as white lies or small deceptions to avoid hurting someone's feelings, lying might be considered acceptable. However, habitual or intentional deception can damage relationships, erode trust, and lead to negative consequences. It's essential to weigh the potential benefits against the potential harm and consider the motivations behind the lie. Ultimately, honesty is usually the best policy, and lying should be a last resort, used sparingly and with caution. Context and intentions play a crucial role.

**Quality Score (0-5):** FP16: ___ | Q4: ___

**Observations:** ___

---
