# cambiar a inglés
reglas_ssml = [
  {
    "role": "user",
    "content": """
    You are going to act as a generator of SSML documents from LaTeX syntax.
     I want you to deconstruct the equation. Do you understand?
     """
  },
  {
    "role": "assistant",
    "content": """
              Sure, for example, if you give me something like \\frac{2}{\\sqrt{4s}}, 
              you would want to distinguish what is the numerator and what is the denominator and generate an SSML
              in which the components of the equation can be distinguished sonically for a visually impaired person.
    """
  },
  {
    "role": "user",
    "content": "Exactly, for example, the prosody rate should be set to slow by default."
  },
  {
    "role": "user",
    "content": """
      For example, for that equation ou gave me, you should aim to have something like:
      <speak>
          <prosody rate="slow"> 
            2 <break time="1s"/>
            over
            <break time="1s"/>
            square root of
            <break time="1s"/>
            4 times
            <break time="1s"/>
            s
          </prosody>
      </speak>
              """
  },
  {
    "role": "user",
    "content": """
      After any element of an equation, add a one-second break,
      the prosody rate should always be slow,
      numbers should always be synthesized as digits.
    """
  },
  {
    "role": "user",
    "content": """
      Remember that this is for visually impaired people, decompose the equation as much as possible
      so that it can be understood for them. For example, I don't want LaTeX syntax in the SSML,
      I don't want a component to be 'frac,' do you understand? That does not contribute anything.
    """
  },
  {
    "role": "user",
    "content": "Also, I have some SSML tags that I want you to use in a predefined way."
  },
  {
    "role": "user",
    "content": """
    I want you to use the tags below so the visually impaired people can hear the difference in some math expressions
    for example, when you are going to write in the SSML the numerator or denominator of a fraction, I want you to use:
          <audio src="https://storage.googleapis.com/ssml-tones/numerator-open.wav"/>
    in the other hand, when the numerator or denominator is going to finish, you will use:
        <audio src="https://storage.googleapis.com/ssml-tones/numerator-close.wav"/>
    in a similar way, when there is a root, you will use the following tag when writing the SSML part of the inside the root
        <audio src="https://storage.googleapis.com/ssml-tones/sqrt-open.wav"/> 
    when it finishes:
        <audio src=" https://storage.googleapis.com/ssml-tones/sqrt-close.wav"/> 
    these are the only audio tags you will use, there is no audios for any other math symbol
    with all of this, for example let's say you have this equation: \\sqrt{\\frac{\\sqrt{x}}{2x}}
    now, with all the tags and everything I have asked ou to do, the SSML should look something like this:

    <speak>
      <prosody rate="slow">
        <audio src="https://storage.googleapis.com/ssml-tones/sqrt-open.wav"/>
          square root of <break time="1s"/>
          <audio src="https://storage.googleapis.com/ssml-tones/numerator-open.wav"/>
          square root of <break time="1s"/>
          <audio src="https://storage.googleapis.com/ssml-tones/sqrt-open.wav"/>
          x <break time="1s"/>
          <audio src="https://storage.googleapis.com/ssml-tones/sqrt-close.wav"/>
          <audio src="https://storage.googleapis.com/ssml-tones/numerator-close.wav"/>
          over <break time="1s"/>
          <audio src="https://storage.googleapis.com/ssml-tones/numerator-open.wav"/>
          2 times <break time="1s"/>
          x <break time="1s"/>
          <audio src="https://storage.googleapis.com/ssml-tones/numerator-close.wav"/>
          <audio src="https://storage.googleapis.com/ssml-tones/sqrt-close.wav"/>
      </prosody>
    </speak>    

    Please, when there is something inside parethesis or a group symbol, don't add the break-time tag, for example for a \\cos(3+3x) don't add the break time between the sum of 3 and 3+
    Note that is the same tag for both numerator and denominator
    Note that the audio is after the root, so it is used to let visually impaired people notice what is inside the root,
    it is the same case with numerator and any other elemente, the audio let people know what is inside that element
    there is no other audio for other math expressions, there is no audio frac-open audio, don't use it, just numerator, and that MUST be used for both numerator and denominator
    """
  },
  {
    "role": "user",
    "content": """
    Remember to just give me the SSML, I do not want any details or extra comments, 
    please, only the SSML, and I do not want encoded symbols, for example, these: <>.
    """
  },
  {
    "role": "user",
    "content": "Don't forget that all the SSML must be within a unique <speak> tag so it can be read and do not forget to close the speak tag for each equation with </speak>"
  },
  {
    "role": "user",
    "content": "There will be just one <speak> for the equation"
  },
  {
    "role": "user",
    "content": "The equation I want you to transform into SSML now is:"
  }
]

reglas_detail = [
  {
    "role": "user",
    "content": """
    You are going to detail equations from latex syntax to natural language, do you understand?
     """
  },
  {
    "role": "assistant",
    "content": """
    Yes! I will give you details so you can understand the equation without even looking at it
     """
  },
  {
    "role": "user",
    "content": """
    That's perfect because I want you to detail the equation so visually impaired people can understand them.
    They are the objective people, so please detail it for them, I don't need the explanation of what the equation is used for
    I just want the structure of the equation to be clear for visually impaired people, but don't be so descriptive
    for example:
      something that is equal to a fraction that is squared, the numerator is... , the denominator is ... and it has a square root of ... 
    that's a simple example, but follow that in order to generate the description, of course you won't use the previous example literally, it's just a guide, for example you won't generate a response that says something is equal, that was just an example
    but of course you also won't use technical language, because visually impaired people wont'understand, just tell them about the terms, not the meaning
    remember not to use symbols for example (^) in order to express something, put that in words
     """
  },
  {
    "role": "user",
    "content": """
    Just give me the description, nothing else, I do not want anything else except for the description, do not say anything else please
    Don't explain so much, be concise about the equation, don't add notes, the description MUST be short
     """
  },
]