
\subsection{Simulating the CLT}
We're finally here! It's time to see whether all of the theory checks out, and the sum of exponentially distributed random variables is itself normally distributed in the simulated limit. We have a Gaussian random number generator based on the sum of exponentially distributed random variables. The easiest way to see whether this generator is actually Gaussian is by plotting it. Before plotting a histogram of our data, though, we are going to normalize so that the resulting plot is normally distributed ($\mu = 0$ and $\sigma = 1$). Recall that creating a normalized variable $X'$ from $X$ involves the following computation:
\[ X' = \frac{X - \mu}{\sigma}\]

So how on earth are we going to do this programmatically? We begin like we always do, by breaking up the problem into smaller parts. We will have to compute $\mu$, the mean, and $\sigma$, the standard deviation of our data. But what is ``our data"? The best representation would be an array, because we need to store each datum in an easily accessable location. Note that C does not support arrays. You will need to implement them from scratch, which is outside the scope of this chapter. Because of this, we're going to leave our dear friend C at this point and proceed with Python.

Let's recap. At this point, we know that we will have to draw $n$ numbers from our \texttt{gaussian\_CLT} method and place them into an array. We will then use this array to compute the mean and standard deviation of the data. Last, we will normalize each element of the array. Now, if we plot a histogram of the data held in this array, it should be a normally distributed bell curve. Because computing the mean, standard deviation, normalization, and plotting are all seperate functions, each of these code blocks should be exported to a seperate method. The driver code, on the other hand, will be the framework of our program so it can be written as our main method and placed at the bottom of our code.

Let's begin with computing the mean. Given an array, we want to sum up all of the elements in that array and divide by the number of items (its length). Fortunately, Python gives us the built-in \texttt{sum()} and \texttt{len()} methods, which compute the sum and length of arrays, respectively. This makes our code easy:

\begin{verbatim}
def mean(array):
    return sum(array) / float(len(array))
\end{verbatim}

The reason we passed \texttt{len(array)} to \texttt{float()} (we could have also said ``casted into a float") is because Python needs the denominator of a fraction to be a decimal if the quotient is to be a decimal. Calling \texttt{float()} performs this cast.

Now on to the standard deviation. Recall that the definition of $\sigma$ is
\[\sigma\ =\ \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - \mu)^2}.\]

Since \task we will need to access each element of data, we will need the data array passed as a parameter to our standard deviation method. At this point, you have seen every operation we will have to perform. We will use the \texttt{sqrt} method from the \texttt{math} library to compute square roots. I am going to start removing the training wheels and give you the code right off the bat. Take a moment and try to write this method yourself. Really. Here's a hint: you should use a \texttt{for} loop. How did it go? In any case, here's the code.

\begin{verbatim}
def std_dev(array):
    n = float(len(array))
    mu = mean(array)
    ss = 0

    # compute the sum of squares
    for x in array:
        ss += ( (x - mu) * (x - mu) )

    return sqrt(ss / n)
\end{verbatim}

Note that we avoided using our bit-shifting trick from before because that only works for integers, and \texttt{x - mu} is a \texttt{float}.

On to data normalization! This method should take the data array as a parameter and return a new, normalized dataset. All it has to do is compute the mean, standard deviation, then loop through the data array setting each $x_i$ to $x_i'$. The code is as follows:

\begin{verbatim}
def normalize(array):
    mu = mean(array)
    sigma = std_dev(array)

    for i in range(len(array)):
        array[i] = (array[i] - mu) / sigma

    return array
\end{verbatim}

On to the driver code, or ``main method". We want to draw $n$ numbers from the exponential distribution, placing each element into an array. We then want to plot a histogram of the normalized data. We will use the family of \texttt{plt} functions from the \texttt{matplotlib.pyplot} library to create these histograms. It would be nice if users could enter their desired value for $n$ when the run the program. We can do this by using the \texttt{argv} array in the \texttt{sys} package. Our code is as follows:

\begin{verbatim}
import matplotlib.pyplot as plt
from sys import argv

def hist(x, xlab="Number", title="Histogram", ylab = 'Frequency'):
    plt.hist(x, bins=25, color='blue')
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.title(title)
    plt.show()

N = int(argv[1])

data = []
for _ in range(N):
  data.append(gaussian_CLT(100))

hist(normalize(data))
\end{verbatim}

Note that all of the items kept in \texttt{argv[]} are strings, so we need to transorm it into an integer by calling \texttt{int()}. We arbitrarally chose 100 for the number of exponential summands. Also note the underscore in the declaration of our foor loop. This lets Python know that we don't need a variable to keep track of each iteration and that we just want to execute the statements in the body of the loop $n$ times.

Phew!! We're finally done! Let's look at out entire program one more time, then run it and see if all of this work paid off. Here's the code:
\scriptsize
\begin{verbatim}
import matplotlib.pyplot as plt
from random import random
from math import log, sqrt
from sys import argv


def hist(x, xlab="Number", title="Histogram", ylab = 'Frequency'):
    plt.hist(x, bins=25, color='blue')
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.title(title)
    plt.show()

def coin_flip(p = 0.5):
    if random() < p:
        return 1.0
    else:
        return 0.0

def uniform(n = 30):
    denominator = 2
    sum = 0.0
    for i in range(n):
        sum += (coin_flip() / denominator)
        denominator <<= 1
    return sum

def exponential(lmbda = 2):
    y = uniform()
    return -lmbda * log(1 - y)

def gaussian(mean = 0, stdDev = 1):
    d = 1.0
    while (d >= 1.0 or d == 0):
        x = uniform() * 2 - 1
        y = uniform() * 2 - 1
        d = x * x + y * y

    d = sqrt( (-2.0 * log(d)) / d )

    return mean + std_dev * d * x

def gaussian_CLT(n):
    x = 0.0
    for _ in range(n):
        x += exponential()

    return x

def mean(array):
    return sum(array) / float(len(array))

def std_dev(array):
    n = float(len(array))
    mu = mean(array)
    ss = 0
    for x in array:
        ss += ((x - mu) * (x - mu))
    return sqrt(ss / n)

def normalize(array):
    mu = mean(array)
    sigma = std_dev(array)

    for i in range(len(array)):
        array[i] = (array[i] - mu) / sigma

    return array


N = int(argv[1])

data = []
for _ in range(N):
    data.append(gaussian_CLT(100))

hist(normalize(data))
\end{verbatim}
\normalsize

Notice that all of our library references are at the top, all of our method definitions are in the body, and our driver code is at the end of our program. Let's run it!

\begin{figure}
\begin{center}
\scalebox{.5}{\includegraphics{10.eps}}
\caption{This was created with $n=10$, using the line \texttt{python code.py 10}. It looks like the $n$ we chose is too small. Let's bump it up a few orders of magnitude.}
\end{center}\end{figure}


\begin{figure}
\begin{center}
\scalebox{.5}{\includegraphics{1000.eps}}
\caption{$n = 1000$, \texttt{python code.py 1000}. Better...}
\end{center}\end{figure}


\begin{figure}
\begin{center}
\scalebox{.5}{\includegraphics{10000.eps}}
\caption{$n = 10000$, \texttt{python code.py 100000}. Looks pretty good! I guess the CLT is true after all!}
\end{center}\end{figure}

If you wish to download this code and try running it yourself, visit \url{https://github.com/rpryzant93/CLT_simulator/blob/master/CLT_simulator.py}.
