import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)




def prepare_sequence(seq, to_idx):
    idxs = [to_idx[w] for w in seq]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)


training_data = [
    ("The dog ate the apple".split(), ["DET", "NN", "V", "DET", "NN"]),
    ("Everybody read that book".split(), ["NN", "V", "DET", "NN"])
]

word_to_idx = {}
for sent, tags in training_data:
    for word in sent:
        if word not in word_to_idx:
            word_to_idx[word] = len(word_to_idx)
print(word_to_idx)
tag_to_idx = {"DET": 0, "NN": 1, "V": 2}


EMBEDDING_DIM = 6
HIDDEN_DIM = 6


class LSTMTagger(nn.Module):
    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
        self.hidden = self.init_hidden()

    def init_hidden(self):
        # each is [layers, batch size, hidden]
        return (
            autograd.Variable(torch.zeros(1, 1, self.hidden_dim)),
            autograd.Variable(torch.zeros(1, 1, self.hidden_dim)))

    def forward(self, sentence):
        embeds = self.word_embeddings(sentence)
        lstm_out, self.hidden = self.lstm(
            embeds.view(len(sentence), 1, -1), self.hidden)
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1))
        tag_scores = F.log_softmax(tag_space)
        return tag_scores




model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(word_to_idx), len(tag_to_idx))
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# See what the scores are before training
# Note that element i,j of the output is the score for tag j for word i.
inputs = prepare_sequence(training_data[0][0], word_to_idx)
tag_scores = model(inputs)
print(tag_scores)

for epoch in range(300):
    for sentence, tags in training_data:
        model.zero_grad()
        model.hidden = model.init_hidden() # clear out hidden state from prev run

        sent_in = prepare_sequence(sentence, word_to_idx)
        targets = prepare_sequence(tags, tag_to_idx)

        tag_scores = model(sent_in)

        loss = loss_function(tag_scores, targets)
        loss.backward()
        optimizer.step()


inputs = prepare_sequence(training_data[0][0], word_to_idx)
tag_scores = model(inputs)
print(tag_scores)


