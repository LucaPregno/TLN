import numpy as np


class Hypothesis(object):

    def __init__(self, tokens, log_probs):
        self._tokens = tokens
        self._log_probs = log_probs

    def extend(self, token, log_prob):
        return Hypothesis(self._tokens+[token],
                          self._log_probs+[log_prob])

    @property
    def last_token(self):
        return self._tokens[-1]

    @property
    def log_prob(self):
        return sum(self._log_probs)

    @property
    def length(self):
        return len(self._tokens)

    @property
    def avg_log_prob(self):
        return self.log_prob / self.length

    @property
    def tokens(self):
        return self._tokens


def beam_search(model, vocab, hps, random=False):
    """
    Each iteration search between fan_out paths,
    then take the hps.beam_size with the highest probability
    """
    start_id = vocab.char2id('<s>')
    hyps = [Hypothesis([start_id], [0.0]) for _ in range(hps.beam_size)]
    fan_out = hps.beam_size * 2
    results = []
    data = np.zeros((hps.beam_size, hps.seq_len))
    step = 0

    while step < hps.seq_len and len(results) < hps.beam_size:
        # prepariamo l'input per la rete neurale
        tokens = np.transpose(np.array([h.last_token for h in hyps]))
        data[:, step] = tokens

        all_hyps = []
        all_probs = model.predict(data)
        # per ogni cammino nella beam search
        for i, h in enumerate(hyps):
            # generiamo la distribuzione di probabilità
            probs = list(all_probs[i, step])
            probs = probs / np.sum(probs)
            indexes = probs.argsort()[::-1]
            # scegliamo 2 * beam_size possibili espansioni dei cammini
            for j in range(fan_out):
                # aggiungere ad all_hyps l'estensione delle ipotesi
                # con il j-esimo indice e la sua probabilità
                if random:
                    index = np.random.choice(range(vocab.size), p=probs)
                else:
                    index = indexes[j]
                all_hyps.append(
                    h.extend(token=index, log_prob=probs[index])
                )

        # teniamo solo beam_size cammini migliori
        hyps = []
        for h in sort_hyps(all_hyps):
            if h.last_token == vocab.char2id("</s>"):
                results.append(h)
            else:
                hyps.append(h)

            if len(hyps) == hps.beam_size or len(results) == hps.beam_size:
                break

        # aggiorniamo data con i token migliori
        if step + 1 < hps.seq_len - 1 and len(hyps) == 5:
            tokens = np.matrix([h.tokens for h in hyps])
            data[:, :step+2] = tokens

        step += 1

    if len(results) == 0:
        results = hyps

    hyps_sorted = sort_hyps(results)

    return hyps_sorted[0]


def sort_hyps(hyps: list):
    # ordinare i cammini in ordine decrescente di probabilità media
    return sorted(hyps, key=lambda x: x.avg_log_prob, reverse=True)

