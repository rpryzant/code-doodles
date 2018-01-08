import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)





# BOW classifier
data = [("me gusta comer en la cafeteria".split(), "SPANISH"),
        ("Give it to me".split(), "ENGLISH"),
        ("No creo que sea una buena idea".split(), "SPANISH"),
        ("No it is not a good idea to get lost at sea".split(), "ENGLISH")]

test_data = [("Yo creo que si".split(), "SPANISH"),
             ("it is lost on me".split(), "ENGLISH")]

word_to_idx = {}
for sent, _ in data + test_data:
    for word in sent:
        if word not in word_to_idx:
            word_to_idx[word] = len(word_to_idx)
label_to_idx = {
    "SPANISH": 0,
    "ENGLISH": 1
    }


VOCAB_SIZE = len(word_to_idx)
NUM_LABELS = 2

class BoWClassifier(nn.Module):
    def __init__(self, num_labels, vocab_size):

        super(BoWClassifier, self).__init__()
        self.linear = nn.Linear(vocab_size, num_labels)


    def forward(self, bow_vec):
        return F.log_softmax(self.linear(bow_vec))

def make_bow_vector(sent, word_to_idx):
    vec = torch.zeros(len(word_to_idx))
    for word in sent:
        vec[word_to_idx[word]] += 1
    # convert to column
    return vec.view(1, -1)

def make_target(label, label_to_idx):
    return torch.LongTensor([label_to_idx[label]])



model =  BoWClassifier(NUM_LABELS, VOCAB_SIZE)

sample = data[0]
v = make_bow_vector(sample[0], word_to_idx)
log_probs = model(autograd.Variable(v))


print next(model.parameters())[:, word_to_idx["creo"]]


loss_fn = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    for instance, label in data:
        model.zero_grad()
        v = autograd.Variable(make_bow_vector(instance, word_to_idx))
        target = autograd.Variable(make_target(label, label_to_idx))

        log_probs = model(v)

        loss = loss_fn(log_probs, target)
        loss.backward()
        optimizer.step()

print next(model.parameters())[:, word_to_idx["creo"]]
