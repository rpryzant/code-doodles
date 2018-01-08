import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

V_data = [1., 2., 3.]
V = torch.Tensor(V_data)
print V.shape


x = autograd.Variable(torch.Tensor([1., 2., 3]), requires_grad=True)
y = autograd.Variable(torch.Tensor([4., 5., 6]), requires_grad=True)
z = x + y
print z.data
print z.grad_fn


print x.grad

s = z.sum()
s.backward()
print x.grad






