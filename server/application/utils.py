def get_sentences_from(text):
    return list(
      map(
        lambda sentence: sentence.strip(),
        filter(
          lambda sentence: len(sentence) > 0,
          text.strip().split('.')
        )
      )
    )
