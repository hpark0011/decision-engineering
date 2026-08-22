---
source_url: https://web.stanford.edu/class/cs379c/class_messages_listing/curriculum/Biographical_Personal/figures/John_von_Neumann1956probabilistic_logics.pdf?utm_source=chatgpt.com
ingested: 2026-08-20
sha256: eb042e381a1b019657f6a14337af6401fda4bccb3b71253d03b558f78d91060c
---

# Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components

J. von Neumann; lectures delivered at the California Institute of Technology, January 4-15, 1952; notes by R. S. Pierce. Published in Automata Studies, edited by C. E. Shannon and J. McCarthy, 1956. This Stanford edition was prepared by Michael D. Godfrey in 2010 from the original Caltech version.

Extraction note: Text was extracted from the 66-page Stanford PDF with pypdf. PDF page markers are retained. Mathematical notation may contain extraction artifacts, and scanned figures are not represented in the text.

<!-- PDF page 1 -->

Lectures on
PROBABILISTIC LOGICS AND THE SYNTHESIS OF RELIABLE
ORGANISMS FROM UNRELIABLE COMPONENTS
delivered by
PROFESSOR J. von NEUMANN
The Institute for Advanced Study
Princeton, N. J.
at the
CALIFORNIA INSTITUTE OF TECHNOLOGY
January 4-15, 1952
Notes by
R. S. PIERCE


<!-- PDF page 2 -->

ii Publication Chronology
Publication Chronology for von Neumann’s
PROBABILISTIC LOGICS AND THE SYNTHESIS OF RELIABLE
ORGANISMS FROM UNRELIABLE COMPONENTS
The following lists the versions of the von Neumann lectures that exist at Caltech or
that have been published. There are 2 versions at Caltech and 3 published versions.
It appears that the most nearly correct version is the ﬁrst Caltech version [1] (See
References, p. iii). Quite a few errors were introduced when the version for [3] was
prepared. It appears that this second version was intended as an “improved” version
for publication. All three of the published versions appear to be based on the ﬁrst
publication ([3]).
Signiﬁcant features of the versions include:
[1] This typescript, with the math drawn by hand, is the only version that includes
the “Analytical Table of Contents.”
[2] This is a Caltech copy of the published version [3]. It is available online at:
http://www.dna.caltech.edu/courses/cs191/paperscs191/VonNeumann56.pdf.
This version also includes a few handwritten notes. It is likely that it was
marked up at Caltech sometime after 1956. The handwritten text is not in-
cluded in the published versions. (The URL is from within the Course Notes for
BE/CS/CNS/Bi 191ab taught by Eric Winfree, 2nd and third terms, 2010,
URL: http://www.dna.caltech.edu/courses/cs191/)
[3] Publication in Automata Studies. The text is somewhat diﬀerent from [1], pos-
sibly edited by von Neumann. It is still a typescript, but with typewriter set
mathematics. (Likely using a new IBM math-capable typewriter.) The Figures
were redrawn. These Figures are cleaner, but a number of errors were introduced.
Speciﬁcally, Figure 4 is in error: the right-hand circuit should have threshold 2.
Figure 9 has no outputs shown. Figure 11 has an incorrect cross-over in the a−1
circuit. Figure 27 has an incorrect point label ( ϵ0) on x-axis. Figure 28 has an
incorrect label on the right side of the left-hand ﬁgure (ρ instead ofQ). Figure 33
has the upper right corner missing. Figure 38 is missing tick marks for αo. Figure
44 is missing (ν = 3) on y-axis. This version is still a typescript, but was re-typed
using a typewriter that provided math symbols, but not calligraphic letters.
[4] This version is based on [3], but was reset in type. It uses the same Figures as
[3].
[5] This version is from [4] without resetting the type. Someone made several hand
corrections to the Figures (including some of the errors noted above). It is possible
that they had access to [1]. Of the three published versions, [5] appears to be the
most nearly correct.
The version that follows here is based on the original version [1], with additional
checking of subsequent versions for useful changes or corrections. The text has been
converted to TEX but the Figures are, at present, scanned from the original [1].


<!-- PDF page 3 -->

Publication Chronology iii
References
[1] J. von Neumann, “PROBABILISTIC LOGICS AND THE SYNTHESIS OF RE-
LIABLE ORGANISMS FROM UNRELIABLE COMPONENTS,” lectures deliv-
ered at the California Institute of Technology, January 4-15, 1952. Notes by R.
S. Pierce, Caltech Eng. Library, QA.267.V6
[2] J. von Neumann, “PROBABILISTIC LOGICS AND THE SYNTHESIS OF RE-
LIABLE ORGANISMS FROM UNRELIABLE COMPONENTS,” with the an-
notation hand-written on the cover page: “Automata Studies, ed C. Shannon,
1956, Princeton Univ Press.”
[3] Published in Automata Studies, eds. C. E. Shannon and J. McCarthy, Princeton
University Press, Annals of Mathematics Studies, No. 34, pp. 43-98, 1956.
[4] Published in John Von Neumann, Collected Works, Vol. 5, ed. A. H. Taub, Perg-
amon Press, pp. 329–378, 1963.
[5] Published in the Babbage Series on the History of Computing, vol. 12, Ch. 13.
pp. 553–603.
Michael D. Godfrey
Stanford University
June 2010


<!-- PDF page 4 -->




<!-- PDF page 5 -->

ANALYTICAL TABLE OF CONTENTS v
ANALYTICAL TABLE OF CONTENTS
Page
1 Introduction................................................................. 1
2 A schematic view of automata. ............................................... 2
2.1 Logics and automata. .................................................... 2
2.2 Deﬁnitions of the fundamental concepts. ................................. 2
2.3 Some basic organs. ...................................................... 4
3 Automata and the propositional calculus. ..................................... 5
3.1 The propositional calculus. .............................................. 5
3.2 Propositions, automata and delays. ...................................... 6
3.3 Universality. General logical considerations. .............................. 7
4 Basic organs. ................................................................ 9
4.1 Reduction of the basic components. ...................................... 9
4.1.1 The simplest reductions. .......................................... 9
4.1.2 The double line trick. ............................................. 9
4.2 Single basic organs. ...................................................... 12
4.2.1 The Scheﬀer stroke. ............................................... 12
4.2.2 The majority organ. ............................................... 13
5 Logics and information. ...................................................... 14
5.1 Intuitionistic logics. ..................................................... 14
5.2 Information. ............................................................ 15
5.2.1 General observations. .............................................. 15
5.2.2 Examples. ........................................................ 15
6 Typical syntheses of automata. ............................................... 16
6.1 The memory unit. ....................................................... 16
6.2 Scalers. ................................................................. 17
6.3 Learning. ............................................................... 19
7 The role of error.............................................................. 21
7.1 Exempliﬁcation with the help of the memory unit. ........................ 21
7.2 The general deﬁnition. ................................................... 22
7.3 An apparent limitation. .................................................. 22
7.4 The multiple line trick. .................................................. 22


<!-- PDF page 6 -->

vi ANALYTICAL TABLE OF CONTENTS
8 Control of error in single line automata. ....................................... 23
8.1 The simpliﬁed probability assumption. ................................... 23
8.2 The majority organ. ..................................................... 23
8.3 Synthesis of automata. .................................................. 24
8.3.1 The heuristic argument. ........................................... 24
8.3.2 The rigorous argument. ............................................ 26
8.4 Numerical evaluation. .................................................. 29
9 The technique of multiplexing................................................. 30
9.1 General remarks on multiplexing. ........................................ 30
9.2 The majority organ. ..................................................... 30
9.2.1 The basic executive organ. ......................................... 30
9.2.2 The need for a restoring organ. .................................... 30
9.2.3 The restoring organ. ............................................... 31
9.2.3.1 Construction. ............................................. 31
9.2.3.2 Numerical evaluation. ..................................... 32
9.3 Other basic organs. ...................................................... 33
9.4 The Scheﬀer stroke. ..................................................... 34
9.4.1 The executive organ. .............................................. 34
9.4.2 The restoring organ. ............................................... 34
10 Error in multiplex systems.................................................... 37
10.1 General remarks......................................................... 37
10.2 The distribution of the response set size. ................................. 38
10.2.1 Exact theory...................................................... 38
10.2.2 Theory with errors. ............................................... 40
10.3 The restoring organ...................................................... 41
10.4 Qualitative evaluation of the results. ..................................... 42
10.5 Complete quantitative theory............................................. 42
10.5.1 General results. ................................................... 43
10.5.2 Numerical evaluation.............................................. 43
10.5.3 Examples. ........................................................ 45
10.5.3.1 First example............................................. 45
10.5.3.2 Second example........................................... 45
10.6 Conclusions. ............................................................ 46
10.7 The general scheme of multiplexing. ...................................... 46
11 General comments on digitalization and multiplexing. ......................... 47
11.1 Plausibility of various assumptions regarding the digital vs. analog
character of the nervous system. ..................................... 47
11.2 Remarks concerning the concept of a random permutation. ............... 48
11.3 Remarks concerning the simpliﬁed probability assumption. ................ 50


<!-- PDF page 7 -->

ANALYTICAL TABLE OF CONTENTS vii
12 Analog possibilities........................................................... 50
12.1 Further remarks concerning analog procedures. ........................... 50
12.2 A possible analog procedure. ............................................. 51
12.2.1 The set up. ....................................................... 51
12.2.2 The operations. ................................................... 52
12.3 Discussion of the algebraical calculus resulting from the above operations. . 52
12.4 Limitations of this system. ............................................... 54
12.5 A plausible analog mechanism: Density modulation by fatigue. ............ 54
12.6 Stabilization of the analog system. ....................................... 55
13 Concluding remark........................................................... 57
13.1 A possible neurological interpretation. .................................... 57
References................................................................... 58


<!-- PDF page 8 -->




<!-- PDF page 9 -->

PROBABILISTIC LOGICS AND THE SYNTHESIS OF RELIABLE
ORGANISMS FROM UNRELIABLE COMPONENTS
By J. von Neumann
1. INTRODUCTION
The paper which follows is based on notes taken by R. S. Pierce on ﬁve lectures given
by the author at the California Institute of Technology in January 1952. They have
been revised by the author, but they reﬂect, apart from stylistic changes, the lectures
as they were delivered. The author intends to prepare an expanded version for pub-
lication, and the present write up, which is imperfect in various ways, does therefore
not represent the ﬁnal and complete publication. That will be more detailed in several
respects, primarily in the mathematical discussions of Sections 9 and 10 (especially
in 10.2 (p. 38) and 10.5.2 (p. 43)), and, also in some of the parts dealing with logics
and with the synthesis of automata. The neurological connections may then also be
explored somewhat further. The present write up is nevertheless presented in this
form because the ﬁeld is in a state of rapid ﬂux, and therefore for ideas that bear on
it an exposition without too much delay seems desirable.
The analytical table of contents which precedes this will give a reasonably close
orientation about the contents – indeed the title should be fairly self explanatory.
The subject-matter is the role of error in logics, or in the physical implementation: of
logics – in automata-synthesis. Error is viewed, therefore, not as an extraneous and
misdirected or misdirecting accident, but as an essential part of the process under
consideration – its importance in the synthesis of automata being fully comparable to
that one of the factor which is normally considered, the intended and correct logical
structure.
Our present treatment of error is unsatisfactory and ad. hoc. It is the author’s
conviction, voiced over many years, that error should be treated by thermodynamical
methods and be the subject of a thermodynamical theory, as information has been by
the work of L. Szilard and C. E. Shannon. (Cf. 5.2 (p. 15)). The present treatment
falls far short of achieving this, but it assembles, it is hoped, some of the building
materials which will have to enter into the ﬁnal structure.
The author wants to express his thanks to K. A. Br¨ uckner and M. Gell-Mann, then
at the University of Illinois, to discussions with whom in 1951 he owes some important
stimuli on this subject; to R. S. Pierce at the California Institute of Technology, on
whose excellent notes this exposition is based; and to the California Institute of
Technology whose invitation to deliver these lectures combined with the very warm
reception by the audience caused him to write this paper in its present form.


<!-- PDF page 10 -->

2 Probabilistic Logics
2. A SCHEMATIC VIEW OF AUTOMATA
2.1 Logics and Automata
It has been pointed out by A. M. Turing [5] in 1937 and by W. S. McCulloch and W.
Pitts [2] in 1943 that eﬀectively constructive logics, that is, intuitionistic logics, can
be best studied in terms of automata. Thus logical propositions can be represented as
electrical networks or (idealized) nervous systems. Whereas logical propositions are
builtup by combining certain primitive symbols, networks are formed by connecting
basic components, such as relays in electrical circuits and neurons in the nervous
system. A logical proposition is then represented as a “black box” which has a ﬁnite
number of inputs (wires or nerve bundles) and a ﬁnite number of outputs. The
operation performed by the box is determined by the rules deﬁning which inputs,
when stimulated, cause responses in what outputs, just as a propositional function is
determined by its values for all possible assignments of values to its variables.
There is one important diﬀerence between ordinary logic and the automata which
represent it. Time never occurs in logic, but every network or nervous system has
a deﬁnite time lag between the input signal and the output response. A deﬁnite
temporal sequence is always inherent in the operation of such a real system. This is
not entirely a disadvantage. For example, it prevents the occurrence of various kinds
of more or less overt vicious circles (related to “non-constructivity,” “impredicativity,”
and the like) which represent a major class of dangers in modern logical systems. It
should be emphasized again, however, that the representative automaton contains
more than the content of the logical proposition which it symbolizes – to be precise,
it embodies a deﬁnite time lag.
Before proceeding to a detailed study of a speciﬁc model of logic, it is necessary
to add a word about notation. The terminology used in the following is taken from
several ﬁelds of science; neurology, electrical engineering, and mathematics furnish
most of the words. No attempt is made to be systematic in the application of terms,
but it is hoped that the meaning will be clear in every case. It must be kept in mind
that few of the terms are being used in the technical sense which is given to them in
their own scientiﬁc ﬁeld. Thus, in speaking of a neuron we don’t mean the animal
organ, but rather one of the basic components of our network which resembles an
animal neuron only superﬁcially, and which might equally well have been called an
electrical relay.
2.2 Deﬁnitions of the fundamental concepts.
Externally an automaton is a “black box” with a ﬁnite number of inputs and a ﬁnite
number of outputs. Each input and each output is capable of exactly two states, to
be designated as the “stimulated” state and the “unstimulated” state, respectively.
The internal functioning of such a “black box” is equivalent to a prescription which


<!-- PDF page 11 -->

A Schematic View of Automata 3
speciﬁes what outputs will be stimulated in response to the stimulation of any given
combination of the inputs, and also of the time of stimulation of these outputs. As
stated above, it is deﬁnitely assumed that the response occurs only after a time lag,
but in the general case the complete response may consist of a succession of responses
occurring at diﬀerent times. This description is somewhat vague. To make it more
precise it will be convenient to consider ﬁrst automata of a somewhat restricted type
and to discuss the synthesis of the general automaton later
DEFINITION 1: A single output automaton with time delay δ (δ is positive) is
a ﬁnite set of inputs, exactly one output, and an enumeration of certain “preferred”
subsets of the set of all inputs. The automaton stimulates its output at time t +δ if
and only if at time t the stimulated inputs constitute a subset which appears in the
list of “preferred” subsets describing the automaton.
In the above deﬁnition the expression “enumeration of certain subsets” is taken
in its widest sense and does not exclude the extreme cases “all” or “none.” If n is
the number of inputs, then there exist 2 (2n) such automata for any given δ.
Frequently several automata of this type will have to be considered simultane-
ously. They need not all have the same time delay, but it will be assumed that all
their time lags are integral multiples of a common valueδ0. This assumption may not
be correct for an actual nervous system; the model considered may apply only to an
idealized nervous system. In partial justiﬁcation, it can be remarked that as long as
only a ﬁnite number of automata are considered, the assumption of a common value
δ0 can be realized within any degree of approximation. Whatever its justiﬁcation
and whatever its meaning in relation to actual machines or nervous systems, this
assumption will be made in our present discussions. The common value δ0 is chosen
for convenience as the time unit. The time variable can now be made discrete, i. e. it
need assume only integral numbers as values, and correspondingly the time delays of
the automata considered are positive integers.
Single output automata with given time delays can be combined into a new au-
tomaton. The outputs of certain automata are connected by lines or wires or nerve
ﬁbers to some of the inputs of the same or other automata. The connecting lines
are used only to indicate the desired connections; their function is to transmit the
stimulation of an output instantaneously to all the inputs connected with that out-
put. The network is subjected to one condition, however. Although the same output
may be connected to several inputs, only one input is assumed to be connected to
at most one output. It may be clearer to impose this restriction on the connecting
lines, by requiring that each input and each output be attached to exactly one line,
to allow lines to be split into several lines; but prohibit the merging of two or more
lines. This convention makes it advisable to mention again that the activity of an
output or an input, and hence of line, is an all or nothing process. If a line is split,
the stimulation is carried to all the branches in full. No energy conservation laws
enter into the problem. In actual machines or neurons the energy is supplied by the
neurons themselves from some external source of energy. The stimulation acts only
as a trigger device.
The most general automaton is deﬁned to be any such network. In general it will


<!-- PDF page 12 -->

4 Probabilistic Logics
have several inputs and several outputs and its response activity will be much more
complex than that of a single output automaton with a given time delay. An intrinsic
deﬁnition of the general automaton, independent of its construction as a network,
can be supplied. It will not be discussed here, however.
Of equal importance to the problem of combining automata into new ones is
the converse problem of representing a given automaton by a network of simpler
automata, and of determining eventually a minimum number of basic types for these
simpler automata. As will be shown, very few types are necessary.
2.3 Some basic organs.
The automata to be selected as a basis for the synthesis of all automata will be
called basic organs. Throughout what follows, these will be single output automata.
One type of basic organ is described by Figure 1. It has one output, and may
have any ﬁnite number of inputs. These are grouped into two types: Excitatory and
inhibitory inputs. The excitatory inputs are distinguished from the inhibitory inputs
by the addition of an arrowhead to the former and of a small circle to the latter.
This distinction of inputs into two types does actually not relate to the concept of
inputs, it is introduced as a means to describe the internal mechanism of the neuron.
This mechanism is fully described by the so-called threshold function ϕ(x) written
inside the large circle symbolizing the neuron in Figure 1, according to the following
convention: The output of the neuron is excited at time t + 1 if and only if at time t
the number of stimulated excitatoryh inputs and the number of stimulated inhibitory
inputs ℓ satisfy the relation h≥ ϕ(ℓ). (It is reasonable to require that the function
ϕ(x) be monotone non-decreasing.) For the purposes of our discussion of this subject
it suﬃces to use only certain special classes of threshold functions ϕ(x). E.g.
(1) ϕ(x)≡ψh(x)
{ =0
=∞ for
x<h
x≥h
}
(i.e.<h inhibitions are absolutely ineﬀective,≥h inhibitions are absolutely eﬀective),
or
(2) ϕ(x)≡X h(x)≡x +h
(i.e. the excess of stimulations over inhibitions must be ≥ h). We will use Xh, and
write the inhibition number h (instead of Xh) inside the large circle symbolizing


<!-- PDF page 13 -->

Automata and the Propositional Calculus 5
the neuron. Special cases of this type are the three basic organs shown in Figure
2. These are, respectively, a threshold two neuron with two excitatory inputs, a
threshold one neuron with two excitatory inputs, and ﬁnally a threshold one neuron
with one excitatory input and one inhibitory input.
The automata with one output and one input described by the networks shown
in Figure 3 have simple properties: The ﬁrst one’s output is never stimulated, the
second one’s output is stimulated at all times if its input has been ever (previously)
stimulated. Rather than add these automata to a network, we shall permit lines
leading to an input to be either always non-stimulated, or always stimulated. We
call the latter “grounded” and designate it by the symbol
 and we call the former
“live” and designate it by the symbol
 .
3. AUTOMATA AND THE PROPOSITIONAL CALCULUS
3.1 The Propositional Calculus
The propositional calculus deals with propositions irrespective of their truth. The set
of propositions is closed under operations of negation, conjunction and disjunction.


<!-- PDF page 14 -->

6 Probabilistic Logics
Ifa is a proposition, then “not a,” denoted by a−1 (we prefer this designation to the
more conventional ones –a and∼a), is also a proposition. Ifa,b are two propositions,
then “a and b,” “a or b,” denoted respectively by ab, a+b, are also propositions.
Propositions fall into two sets, T and F, depending whether they are true or false.
The proposition a−1 is in T if and only if a is in F . The proposition ab is in T
if and only if a and b are both in T, and a +b is in T if and only if either a or
b is in T . Mathematically speaking the set of propositions, closed under the three
fundamental operations, is mapped by a homomorphism onto the Boolean algebra of
the two elements 1 and 0. A proposition is true if and only if it is mapped onto the
element 1. For convenience, denote by 1 the proposition ¯a + ¯a1, by 0 the proposition
¯a¯a1, where ¯a is a ﬁxed but otherwise arbitrary proposition. Of course, 0 is false and
1 is true.
A polynomial P in n variables, n≥ 1, is any formal expression obtained from
x1,...,x n by applying the fundamental operations to them a ﬁnite number of times,
for example [( x1 + x−1
2 )x3]−1 is a polynomial. In the propositional calculus two
polynomials in the same variables are considered equal if and only if for any choice
of the propositions x1,...,x n the resulting two propositions are always either both
true or both false. A fundamental theorem of the propositional calculus states that
every polynomialP is equal to
∑
i1=±1
...
∑
in=±1
fi1...inxi1
1 ...x in
n,
where each of the fi1...in is equal to 0 or 1. Two polynomials are equal if and only if
their f’s are equal. In particular, for each n, there exist exactly 2 (2n) polynomials.
3.2 Propositions, automata and delays.
These remarks enable us to describe the relationship between automata and the
propositional calculus. Given a time delay s, there exists a one-to-one correspon-
dence between single output automata with time delay s and the polynomials of the
propositional calculus. The number n of inputs (to be designated ν = 1,...,n ) is
equal to the number of variables. For every combination i1 =±1,...,i n =±1, the
coeﬃcient fi1...in = 1, if and only if a stimulation at time t of exactly those inputs ν
for which iν = 1, produces a stimulation of the output at time t +s.
DEFINITION 2: Given a polynomial P =P(x1...x n) and a time delay s, we mean
by aP,s -network a network built from the three basic organs of Figure 2, which as
an automaton representsP with time delay s.
THEOREM 1: Given any P, there exists a (unique) s∗ = s∗(P), such that a P,s -
network exists if and only if s≥s∗.
PROOF: Consider a givenP. Let S(P) be the set of those s for which aP,s -network
exists. If s′≥s, then tying s′−s unit-delays, as shown in Figure 4, in series to the
output of a P,s -network produces a P,s′-network. Hence S(P) contains with an s
all s′≥ s. Hence if S(P) is not empty, then it is precisely the set of all s≥ s∗,


<!-- PDF page 15 -->

Automata and the Propositional Calculus 7
wheres∗ =s∗(P) is its smallest element. Thus the theorem holds forP ifS(P) is not
empty, i.e. if the existence of at least one P,s -network (for, some s !) is established.
Now the proof can be eﬀected by induction over the number ϱ =ϱ(P) of symbols
used in the deﬁnitory expression for P (counting each occurrence of each symbol
separately).
If ϱ(P) = 1, thenP(xi,...,x n)≡xν (for one of the v = 1,...,n ). The “trivial”
network which obtains by breaking oﬀ all input lines other than ν, and taking the
input line ν directly to the output, solves the problem with s = 0. Hence s∗(P) = 0.
Ifϱ(P)> 1, thenP≡Q −1 orP≡QR orP≡Q +R, whereϱ(Q),ϱ (R)<ϱ (P).
ForP ≡ Q−1 let the box Q represent a Q,s′-network, with s′ = s∗(Q). Then
the network shown in Figure 5 is clearly a P,s -network, with s = s′ + 1. Hence
s∗(P)≤s∗(Q) + 1. ForP≡QR orQ +R let the boxes Q , R represent aQ,s′′-
network and anR,s′′-network, respectively, withs′′ = max(s∗(Q),s∗(R)). Then the
network shown in Figure 6 is clearly a P,s -network, with P ≡QR orQ +R for
h = 2 or 1, respectively, and withs =s′′ + 1. Hence s∗(P)≤ max(s∗(Q),s∗(R)) + 1.
Combine the above theorem with the fact that every single output automaton
can be equivalently described – apart from its time delay s – by a polynomialP, and
that the basic operations ab, a+b, a−1 of the propositional calculus are represented
(with unit delay) by the basic organs of Figure 2. (For the last one, which represents
ab−1, cf. the remark at the beginning of 4.1.1. (p. 9)) This gives:
DEFINITION 3: Two single output automata are equivalent in the wider sense, if
they diﬀer only in their time delays – but otherwise the same input stimuli produce
the same output stimulus (or non-stimulus) in both.
THEOREM 2 (Reduction Theorem): Any single output automaton ϑ is equivalent
in the wider sense to a network of basic organs of Figure 2. There exists a (unique)
s =s∗(ϑ), such that the latter network exists if and only if its prescribed time delay
s satisﬁes s≥s∗.


<!-- PDF page 16 -->

8 Probabilistic Logics
3.3 Universality. General logical considerations.
Now networks of arbitrary single output automata can be replaced by networks of
basic organs of Figure 2: It suﬃces to replace the unit delay in the former system
by ¯s unit delays in the latter, where ¯s is the maximum of the s∗(ϑ) of all the single
output automata that occur in the former system. Then all delays that will have to
be matched will be multiples of ¯s, hence≥ ¯s, hence≥s∗(ϑ) for all ϑ that can occur
in this situation, and so the Reduction Theorem will be applicable throughout.
Thus this system of basic organs is universal: It permits the construction of
essentially equivalent networks to any network that can be constructed from any
system of single output automata. I.e. no redeﬁnition of the system of basic organs
can extend the logical domain covered by the derived networks.
The general automaton is any network of single output automata in the above
sense. It must be emphasized that, in particular, feedbacks, i.e. arrangements of lines
which may allow cyclical stimulation sequences, are allowed. (I.e. conﬁgurations like
those shown in Figure 7, etc. There will be various, non-trivial, examples of this
later.) The above arguments have shown that a limitation of the underlying single
output automata to our original basic organs causes no essential loss of generality.
The question as to which logical operations can be equivalently represented (with
suitable, but not a priori speciﬁed delays) is nevertheless not without diﬃculties.
These general automata are, in particular, not immediately equivalent to all of
eﬀectively constructive (intituitionistic), logics. I.e. given a problem involving (a
ﬁnite number of) variables, which can be solved (identically in these variables) by
eﬀective construction, it is not always possible to construct a general automaton that
will produce this solution identically (i.e under all conditions). The reason for this is
essentially, that the memory requirements of such a problem may depend on (actual
values assumed by) the variables (i.e. they must be ﬁnite for any speciﬁc system of
values of the variables, but they may be unbounded for the totality of all possible
systems of values), while a general automaton in the above sense, necessarily has a
ﬁxed memory capacity. I.e. a ﬁxed general automaton can only handle (identically,
i.e. generally) a problem with ﬁxed (bounded) memory requirements.
We need not go here into the details of this question. Very simple addenda
can be introduced to provide for a (ﬁnite but) unlimited memory capacity. How
this can be done has been shown by A. M. Turing [5]. Turing’s analysis loc. cit.
also shows that with such addenda general automata become strictly equivalent to
eﬀectively constructive (intuitionistic) logics. Our system in its present form (i.e.
general automata with limited memory capacity) is still adequate for the treatment
of all problems with neurological analogies, as our subsequent examples will show.
(Cf. also W. S. McCulloch and W. Pitts [2].) The exact logical domain that they
cover has been recently characterized by Kleene [1]. We will return to some of these
questions in 5.1.


<!-- PDF page 17 -->

Basic Organs 9
4. BASIC ORGANS.
4.1 Reduction of the basic components.
4.1.1 The simplest reductions.
The previous Section makes clear the way in which the elementary neurons should be
interpreted logically. Thus the ones shown in Figure 2 (p. 5) respectively represent
the logical functions ab, a+b, and ab−1. In order to get b−1, it suﬃces to make the
a-terminal of the third organ, as shown in Figure 8 , live. This will be abbreviated
in the following, as shown in Figure 8.
Now sinceab≡ ((a−1) + (b−1))−1 anda +b≡ ((a−1)(b−1))−1, it is clear that the
ﬁrst organ among the three basic organs shown in Figure 2 is equivalent to a system
built of the remaining two organs there, and that the same is true for the second organ
there. Thus the ﬁrst and second organs shown in Figure 2 are respectively equivalent
(in the wider sense) to the two networks shown in Figure 9. This tempts one to
consider a new system, in which
 (viewed as a basic entity in its own right,
and not an abbreviation for a composite, as in Figure 8), and either the ﬁrst or the
second basic organ in Figure 2, are the basic organs. They permit forming the second
or the ﬁrst basic organ in Figure 2, respectively, as shown above, as (composite)
networks. The third basic organ in Figure 2 is easily seen to be also equivalent (in
the wider sense) to a composite of the above but, as was observed at the beginning
of 4.1.1 (p. 9) the necessary organ is in any case not this, but
 (cf. also the
remarks concerning Figure 8), respectively. Thus either system of new basic organs
permits reconstructing (as composite networks) all the (basic) organs of the original
system. It is true, that these constructs have delays varying from 1 to 3, but since
unit delays, as shown in Figure 4, are available in either new system, all these delays
can be brought up to the value 3. Then a trebling of the unit delay time obliterates
all diﬀerences.
To restate: Instead of the three original basic organs, shown again in Figure 10,
we can also (essentially equivalently) use the two basic organs Nos. one and three or
Nos. two and three in Figure 10.


<!-- PDF page 18 -->

10 Probabilistic Logics
4.1.2 The double line trick.
This result suggests strongly that one consider the one remaining combination, too:
The two basic organs Nos. one and two in Figure 10, as the basis of an essentially
equivalent system.
One would be inclined to infer that the answer must be negative: No network
built out of the two ﬁrst basic organs of Figure 10 can be equivalent (in the wider
sense) to the last one. Indeed, let us attribute to T and F, i.e. to the stimulated
or non-stimulated state of a the, respectively, the “truth values” 1 or 0, respectively.
Keeping the ordering 0 < 1 in mind, the state of the output is a monotone non-
decreasing function of the states of the inputs for both basic organs Nos. one and two
in Figure 10, and hence for all networks built from these organs exclusively as well.
This, however is not the case for the last organ of Figure 10 (nor for the last organ
of Figure 2), irrespectively of delays.
Nevertheless a slight change of the underlying deﬁnitions permits one to circum-
vent this diﬃculty and to get rid of the negation (the last organ of Figure 10) entirely.
The device which eﬀects this is of additional methodical interest, because it may be
regarded as the prototype of one that we will use later on in a more complicated sit-
uation. The trick in question is to represent propositions on a double line instead of
single one. One assumes that of the two lines, at all times precisely one is stimulated.
Thus there will always be two possible states of the line pair: The ﬁrst line stimulated,
the second non-stimulated; and the second line stimulated, the ﬁrst non-stimulated.
We let one of these states correspond to the stimulated single line of the original sys-
tem – that is, to a true proposition – and the other state to the unstimulated single
line – that is, to a false proposition. Then the three fundamental Boolean operations
can be represented by the three ﬁrst schemes shown in Figure 11. (The last scheme
shown in Figure 11 relates to the original system of Figure 2.)
In these diagrams, a true proposition corresponds to 1 stimulated, 2 unstimulated,
while a false proposition corresponds to 1 unstimulated, 2 stimulated. The networks
of Figure 11, with the exception of the third one, have also the correct delays: Unit
delay. The third one has zero delay, but whenever this is not wanted, it can be
replaced by unit delay; by replacing the third network by the fourth one, making its
a1-line live, its a2-line grounded, and then writing a for its b.
Summing up: Any two of the three (single delay) organs of Figure 10 – which


<!-- PDF page 19 -->

Basic Organs 11
may simply be designated by ab, a + b, a−1 – can be stipulated to be the ba-
sic organs, and yield a system that is essentially equivalent to the original one.


<!-- PDF page 20 -->

12 Probabilistic Logics
4.2 Single basic organs.
4.2.1 The Scheﬀer stroke.
It is even possible to reduce the number of basic organs to one, although it cannot
be done with any of the three organs enumerated above. We will, however, introduce
two new organs, either of which suﬃces by itself.
The ﬁrst universal organ corresponds to the well-known “Scheﬀer stroke” function.
Its use in this context was suggested by K. A. Br¨ uckner and M. Gell-Mann. In
symbols, it can be represented (and abbreviated) as shown on Figure 12. The three
fundamental Boolean operations can now be performed as shown in Figure 13.
The delays are 2, 2, 1, respectively, and in this case the complication caused by
these delay-relationships is essential. Indeed, the output of the Scheﬀer-stroke is an
antimonotone function of its inputs. Hence in every network derived from it, even-
delay outputs will be monotone functions of its inputs, and anti-delay outputs will be
antimonotone ones. Now ab and a +b are not antimonotone, and ab−1 and a−1 are
not monotone. Hence no delay-value can simultaneously accommodate in this set up
one of the two ﬁrst organs and one of the two last organs.


<!-- PDF page 21 -->

Basic Organs 13
The diﬃculty can, however, be overcome as follows: ab anda +b are represented
in Figure 13, both with the same delay, namely 2. Hence our earlier result (in 4.1.2),
securing the adequacy of the system of the two basic organs ab and a +b applies:
Doubling the unit delay time reduces the present set up (Scheﬀer stroke only!) to the
one referred to above.
4.2.2 The majority organ.
The second universal organ is the “majority organ.” In symbols, it is shown (and
alternatively designated) in Figure 14. To get conjunction and disjunction is a simple
matter, as shown in Figure 15. Both delays are 1. Thus ab and a +b (according to
Figure 10) are correctly represented, and the new system (majority organ only!) is
adequate because the system based on those two organs is known to be adequate (cf.
4.1.2).


<!-- PDF page 22 -->

14 Probabilistic Logics
5. LOGICS AND INFORMATION.
5.1 Intuitionistic logics.
All of the examples which have been described in the last two Sections have had a
certain property in common; in each, a stimulus of one of the inputs at the left could
be traced through the machine until at a certain time later it came out as a stimulus
of the output on the right. To be speciﬁc, no pulse could ever return to a neuron
through which it had once passed. A system with this property is called circle-free
by W. S. McCulloch and W. Pitts [2]. While the theory of circle-free machines is
attractive because of its simplicity, it is not hard to see that these machines are very
limited in their scope.
When the assumption of no circles in the network is dropped, the situation is
radically altered. In this far more complicated case, the output of the machine at
any time may depend on the state of the inputs in the indeﬁnitely remote past. For
example, the simplest kind of cyclic circuit, as shown in Figure 16, is a kind of memory
machine. Once this organ has been stimulated by a, it remains stimulated and sends
forth a pulse in b at all times thereafter. With more complicated networks, we can
construct machines which will count, which will do simple arithmetic, and which
Will will even perform certain unlimited inductive processes. Some of these will be
illustrated by examples in Section 6 (p. 16). The use of cycles or feedback in automata
extends the logic of constructable machines to a large portion of intuitionistic logic.
Not all of intuitionistic logic is so obtained, however, since these machines are limited
by their ﬁxed size. (For this and for the remainder of this Section; cf. also the remarks
at the end of 3.3. (p. 7)) Yet if our automata are furnished with an unlimited memory
– for example an inﬁnite tape, and scanners connected to aﬀerent organs, along with
suitable eﬀerent organs to perform motor operations and/or print on the tape – the
logic of constructable machines becomes precisely equivalent to intuitionistic logic
(see A. M. Turing [5]). In particular, all numbers computable in the sense of Turing
can be computed by some such network.


<!-- PDF page 23 -->

Logics and Information 15
5.2 Information.
5.2.1 General observations.
Our considerations deal with varying situations, each of which contains a certain
amount of information. It is desirable to have a means of measuring that amount. In
most cases of importance, this is possible. Suppose an event is one selected from a
ﬁnite set of possible events. Then the number of possible events can be regarded as
a measure of the information content of knowing which event occurred, provided all
events are a priori equally probable. However, instead of using the numbern of possi-
ble events as the measure of information, it is advantageous to use a certain function
ofn, namely the logarithm. This step can be (heuristically) justiﬁed as follows: If two
physical systems I and II represent n andm (a priori equally probable) alternatives,
respectively, then the union I+II represents nm such alternatives. Now it is desir-
able that the (numerical) measure of information be (numerically) additive under this
(substantively) additive composition I+II. Hence some function f(n) should be used
instead of n, such that
(3) f(nm) =f(n) +f(m).
In addition, for n > mI represents more information than II, hence it is reasonable
to require
(4) n>m implies f(n)>f (m).
Note, that f(n) is deﬁned for n = 1, 2,... only. From (3), (4) one concludes easily,
that
(5) f(n)≡C lnn
for some constant C >0. (Since f(n) is deﬁned for n = 1, 2,... only, (3) alone does
not imply this, even not with a constant C ≤
≥ 0 !) Next, it is conventional to let the
minimum non-vanishing amount of information, i.e. that which corresponds ton = 2,
be the unit of information – the “bit.” This means that f(2) = 1, i.e. C = 1/ log 2.
and so
(6) f(n)≡ 2 logn.
This concept of information was successively developed by several authors in the late
1920’s and early 1930’s, and ﬁnally integrated into a broader system by C. E. Shannon
[3].
5.2.2 Examples
The following simple examples give some illustration: The outcome of the ﬂip of a coin
is one bit. That of the roll of a die is 2 log 6≈ 2.5 bits. A decimal digit represents


<!-- PDF page 24 -->

16 Probabilistic Logics
2 log 10≈ 3.3 bits, a letter of the alphabet represents 2 log 26≈ 4.7 bits, a single
character from a 44-key 2-setting typewriter represents 2 log(44× 2) = 6.5 bits. (In
all these we assume, for the sake of the argument, although actually unrealistically,
a priori equal probability of all possible choices.) It follows that any line or nerve
ﬁber which can be classiﬁed as either stimulated or non-stimulated carries precisely
one bit of information, while a bundle of n such lines can communicate n bits. It
is important to observe that this deﬁnition is possible only on the assumption that
a background of a priori knowledge exists, namely, the knowledge of a system of a
priori equally probable events.
This deﬁnition can be generalized to the case where the possible events are not all
equally probable. Suppose the events are known to have probabilities p1,p 2,...,p n.
Then the information contained in the knowledge of which of these events actually
occurs, is deﬁned to be
(7) H =
n∑
i=1
pi 2 logpi (bits).
In case p1 = p2 = ... = pn = 1/n, this deﬁnition is the same as the previous one.
This result, too, was obtained by C. E. Shannon [3], although it is implicit in the
earlier work of L. Szilard [4].
An important observation about this deﬁnition is that it bears close resemblance
to the statistical deﬁnition of the entropy of a thermodynamical system. If the possible
events are just the known possible states of the system with their corresponding
probabilities, then the two deﬁnitions are identical. Pursuing this, one can construct a
mathematical theory of the communication of information patterned after statistical
mechanics. (See L. Szilard [4] and C. E. Shannon [3].) That information theory
should thus reveal itself as an essentially thermodynamical discipline, is not at all
surprising: The closeness and the nature of the connection between information and
entropy is inherent in L. Boltzmann’s classical deﬁnition of entropy (apart from a
constant, dimensional factor) as the logarithm of the “conﬁguration number.” The
“conﬁguration number” is the number of a priori equally probable states that are
compatible with the macroscopic description of the state – i.e. it corresponds to the
amount of (microscopic) information that is missing in the (macroscopic) description.
6. TYPICAL SYNTHESES OF AUTOMATA.
6.1 The memory unit.
One of the best ways to become familiar with the ideas which have been intro-
duced, is to study some concrete examples of simple networks. This Section is devoted
to a consideration of a few of them.
The ﬁrst example will be constructed with the help of the three basic organs of
Figure 10. It is shown in Figure 18. It is a slight rearrangement of the primitive


<!-- PDF page 25 -->

Typical Syntheses of Automata 17
memory network of Figure 16.
This network has two inputsa andb and one outputx. At time t,x is stimulated
if and only if a has been stimulated at an earlier time, so that no stimulation of b
has occurred since then. Roughly speaking, the machine remembers whether a or b
was the last input to be stimulated. Thus x is stimulated if it has been stimulated
immediately before — to be designated by x′ — or if a has been stimulated immedi-
ately before, but b has not been stimulated immediately before. This is expressed by
the formula x = (x′ +a)b−1, i.e. by the network shown in Figure 17. Now x should
be fed back into x′ (since x′ is the immediately preceding state of x). This gives the
network shown in Figure 18, where this branch of x is designated by y. However,
the delay of the ﬁrst network is 2, hence the second network’s memory extends over
past events that lie an even number of time (delay) units back. I.e. the output x is
stimulated if and only if a has been stimulated at an earlier time, an even number of
units before, so that no stimulation of b has occurred since then, also an even number
of units before. Enumerating the time units by an integer t, it is thus seen that this
network represents a separate memory for even and for odd t. For each case it is a
simple “oﬀ-on,” i.e. one bit, memory. Thus it is in its entirety a two bit memory.
6.2 Scalers.
In the examples that follow, free use will be made of the general family of basic
organs considered in 2.3, at least for all ϕ =χh (cf. (2) there). The reduction thence
to elementary organs in the original sense is secured by the Reduction Theorem in
3.2, and in the subsequently developed interpretations, according to Section 4, by our
considerations there. It is therefore unnecessary to concern ourselves here with these
reductions.
The second example is a machine which counts input stimuli by twos. It will be
called a “scaler by two.” Its diagram is shown in Figure 19.
By adding another input, the repressor, the above mechanism can be turned oﬀ
at will. The diagram becomes as shown in Figure 20. The result will be called a
“scaler by two” with a repressor and denoted as indicated by Figure 20.
In order to obtain larger counts, the “scaler by two” networks can be hooked in
series. Thus a “scaler by 2 n” is shown in Figure 21. The use of the repressor is of
course optional here. “Scalers by m,” where m is not necessarily of the form 2 n, can
also be constructed with little diﬃculty, but we will not go into this here.


<!-- PDF page 26 -->

18 Probabilistic Logics


<!-- PDF page 27 -->

Typical Syntheses of Automata 19
6.3 Learning.
Using these “scalers by 2 n” (i.e. n-stage counters), it is possible to construct the
following sort of “learning device.” This network has two inputs a and b. It is
designed to learn that whenever a is stimulated, then, in the next instant, b will be
stimulated. If this occurs 256 times (not necessarily consecutively and possibly with
many exceptions to the rule), the machine learns to anticipate a pulse fromb one unit
of time aftera has been active, and expresses this by being stimulated at its b output
after every stimulation of a. The diagram is shown in Figure 22. (The“ expression”
described above will be made eﬀective in the desired sense by the network of Figure
24, cf. its discussion below).
This is clearly learning in the crudest and most ineﬃcient way, only. With some
eﬀort, it is possible to reﬁne the machine so that, ﬁrst, it will learn only if it receives
no counter-instances of the pattern “b followsa” during the time when it is collecting
these 256 instances; and, second having once learned, the machine can unlearn by
the occurrence of 64 counter-examples to “ b follows a” if no (positive) instances of
this pattern interrupt the (negative) series. Otherwise, the behavior is as before. The
diagram is shown in Figure 23. To make this learning eﬀective, one has to use x
to gate a so as to replace b at its normal functions. Let these be represented by an
output c. Then this process is mediated by the network shown in Figure 24. This
network must then be attached to the lines a,b and to the output x of the preceding
network (according to Figures 22, 23).


<!-- PDF page 28 -->

20 Probabilistic Logics


<!-- PDF page 29 -->

The Role of Error 21
7. THE ROLE OF ERROR.
7.1 Exempliﬁcation with the help of the memory unit.
In all the previous considerations, it has been assumed that the basic components
were faultless in their performance. This assumption is clearly not a very realistic
one. Mechanical devices as well as electrical ones are statistically subject to failure,
and the same is probably true for animal neurons too. Hence it is desirable to ﬁnd
a closer approximation to reality as a basis for our constructions, and to study this
revised situation. The simplest assumption concerning errors is this: With every basic
organ is associated a positive number such that in any operation, the organ will fail
to function correctly with the (precise) probabilityϵ. This malfunctioning is assumed
to occur statistically independently of the general state of the network and of the
occurrence of other malfunctions. A more general assumption, which is a good deal
more realistic, is this: The malfunctions are statistically dependent on the general
state of the network and on each other. In any particular state, however, a malfunction
of the basic organ in question has a probability of malfunctioning which is ≤ϵ. For
the present occasion, we make the ﬁrst (narrower and simpler) assumption, and that
with a single ϵ: Every neuron has statistically independently of all else exactly the
probability ϵ of misﬁring. Evidently, it might as well be supposed ϵ≤ 1
2, since an
organ which consistently misbehaves with a probability > 1
2, is just behaving with
the negative of its attributed function, and a (complementary) probability of error
< 1
2. Indeed, if the organ is thus redeﬁned as its own opposite, its ϵ(> 1
2) goes then
over into 1−ϵ(< 1
2). In practice it will be found necessary to have ϵ a rather small
number, and one of the objectives of this investigation is to ﬁnd the limits of this
smallness, such that useful results can still be achieved.
It is important to emphasize that the diﬃculty introduced by allowing error is
not so much that incorrect information will be obtained, but rather that irrelevant
results will be produced. As a simple example, consider the memory organ of Figure
16. Once stimulated, this network should continue to emit pulses at all later times;
but suppose it has the probability ϵ of making an error. Suppose the organ receives
a stimulation at time t and no later ones. Let the probability that the organ is still
excited after s cycles be denoted ρs. Then the recursion formula
ρs+1 = (1−ϵ)ρs +ϵ(1−ρs)
is clearly satisﬁed. This can be written
ρs+1− 1
2 = (1− 2ϵ)(ρs− 1
2)
and so
(8) ρs− 1
2 = (1− 2ϵ)s(ρ0− 1
2)≈e−2ϵs(ρ0− 1
2)


<!-- PDF page 30 -->

22 Probabilistic Logics
for small ϵ. The quantity ρs− 1
2 can be taken as a rough measure of the amount of
discrimination in the system after the s-th cycle. According to the above formula,
ρs→ 1
2 as s→∞ – a fact which is expressed by saying that, after a long time, the
memory content of the machine disappears, since it tends to equal likelihood of being
right or wrong. i.e. to irrelevancy.
7.2 The general deﬁnition.
This example is typical of many. In a complicated network, with long stimulus-
response chains, the probability of errors in the basic organs makes the response of
the ﬁnal outputs unreliable, i.e. irrelevant, unless some control mechanism prevents
the accumulation of these basic errors. We will consider two aspects of this problem.
Let the data be these: The function which the automaton is to perform is given; a
basic organ is given (Scheﬀer stroke, for example); a number ϵ (< 1
2), which is the
probability of malfunctioning of this basic organ, is prescribed. The ﬁrst question
is: Given δ > 0, can a corresponding automaton be constructed from the given
organs, which will perform the desired function and will commit an error (in the ﬁnal
result. i.e. output) with probability≤δ? How small canδ be prescribed? The second
question is: Are there other ways to interpret the problem which will allow us to
improve the accuracy of the result?
7.3 An apparent limitation.
In partial answer to the ﬁrst question, we notice now thatδ, the prescribed maximum
allowable (ﬁnal) error of the machine, must not be less than ϵ. For any output of
the automaton is the immediate result of the operation of a single ﬁnal neuron and
the reliability of the whole system cannot be better than the reliability of this last
neuron.
7.4 The multiple line trick.
In answer to the second question, a method will be analyzed by which this threshold
restriction δ≥ ϵ can be removed. In fact we will be able to prescribe δ arbitrarily
small (for suitable, but ﬁxed, ϵ). The trick consists in carrying all the messages
simultaneously on the bundle of N lines ( N is a large integer) instead of just a
single or double strand as in the automata described up to now. An automaton
would then be represented by a black box with several bundles of inputs and outputs,
as shown in Figure 25. Instead of requiring that all or none of the lines of the
bundle be stimulated, a certain critical(or ﬁduciary) level ∆ is set: 0 < ∆< 1
2. The
stimulation of≥ (1− ∆)N lines of a bundle is interpreted as a positive state of the
bundle. The stimulation of ≤ ∆N lines is considered as a negative state. All levels
of stimulation between these values are intermediate or undecided. It will be shown


<!-- PDF page 31 -->

Control of Error in Single Line Automata 23
that by suitably constructing the automaton, the number of lines deviating from the
“correctly functioning” majorities of their bundles can be kept at or below the critical
level ∆N (with arbitrarily high probability). Such a system of construction is referred
to as “multiplexing.” Before turning to the multiplexed automata, however, it is well
to consider the ways in which error can be controlled in our customary single line
networks.
8. CONTROL OF ERROR IN SINGLE LINE AUTOMATA.
8.1 The simpliﬁed probability assumption.
In 7.3 (p. 22) it was indicated that when dealing with an automaton in which messages
are carried on a single (or even a double) line, and in which the components have a
deﬁnite probabilityϵ of making an error, there is a lower bound to the accuracy of the
operation of the machine. It will now be shown that it is nevertheless possible to keep
the accuracy within reasonable bounds by suitably designing the network. For the
sake of simplicity only circle-free automata (cf. 5.1 (p. 14)) will be considered in this
Section, although the conclusions could be extended, with proper safeguards, to all
automata. Of the various essentially equivalent systems of basic organs (cf. Section
4 (p. 9)) it is, in the present instance, most convenient to select the majority organ,
which is shown in Figure 14 (p. 13), as the basic organ for our networks. The number
ϵ(0<ϵ< 1
2) will denote the probability each majority organ has for malfunctioning.
8.2 The majority organ.
We ﬁrst investigate upper bounds for the probability of errors as impulses pass
through a single majority organ of a network. Three lines constitute the inputs
of the majority organ. They come from other organs or are external inputs of the
network. Let η1,η 2,η 3 be three numbers (0 < ηi≤ 1), which are respectively up-
per bounds for the probabilities that these lines will be carrying the wrong impulses.
Then ϵ +η1 +η2 +η3 is an upper bound for the probability that the output line
of the majority organ will act improperly. This upper bound is valid in all cases.
Under proper circumstances it can be improved. In particular, assume: (i) The prob-
abilities of errors in the input lines are independent, (ii) under proper functioning of


<!-- PDF page 32 -->

24 Probabilistic Logics
the network, these lines should always be in the same state of excitation (either all
stimulated, or all unstimulated). In this latter case
Θ =η1η2 +η1η3 +η2η3− 2η1η2η3
is an upper bound for at least two of the input lines carrying the wrong impulses,
and thence
ϵ′ = (1−ϵ)Θ +ϵ(1− Θ) =ϵ + (1− 2ϵ)Θ
is a smaller upper bound for the probability of failure in the output line. If all ηi≤η,
then ϵ + 3η is a general upper bound, and
ϵ + (1− 2ϵ)(3η2− 2η3)≤ϵ + 3η2
is an upper bound for the special case. Thus it appears that in the general case each
operation of the automaton increases the probability of error since ϵ + 3η > η,so
that if the serial depth of the machine (or rather of the process to be performed) is
very great, it will be impractical or impossible to obtain any kind of accuracy. In
the special case, on the other hand, this is not necessarily so ϵ + 3η2<η is possible.
Hence, the chance of keeping the error under control lies in maintaining the conditions
of the special case throughout the construction. We will now exhibit a method which
achieves this.
8.3 Synthesis of Automata.
8.3.1 The heuristic argument.
The basic idea in this procedure is very simple. Instead of running the incoming data
into a single machine, the same information is simultaneously fed into a number of
identical machines, and the result that comes out of a majority of these machines
is assumed to be true. It must be shown that this technique can really be used to
control error.
Denote by O the given network (assume two outputs in the speciﬁc instance
pictured in Figure 26). Construct O in triplicate, labeling the copies O1,O 2,O 3
respectively. Consider the system shown in Figure 26.


<!-- PDF page 33 -->

Control of Error in Single Line Automata 25
For each of the ﬁnal majority organs the conditions of the special case considered
above obtain. Consequently, ifη is an upper bound for the probability of error at any
output of the original network O, then
(9) η∗ =ϵ + (1− 2ϵ)(3η2− 2η3)≡fϵ(η)
is an upper bound for the probability of error at any output of the new network O∗.
The graph is the curve η∗ =fϵ(η), shown in Figure 27.
Consider the intersections of the curve with the diagonal η∗ =η : First, η = 1
2 is
at any rate such an intersection. Dividing η−fϵ(η) byη− 1
2 gives 2((1− 2ϵ)η2− (1−
2ϵ)η +ϵ), hence the other intersections are the roots of (1− 2ϵ)η2− (1− 2ϵ)η +ϵ = 0,
i.e.
η = 1
2
(
1±
√
1− 6ϵ
1− 2ϵ
)
I.e. for ϵ≥ 1
6 they do not exist (being complex (for ϵ> 1
6) or = 1
2 (for ϵ = 1
6)); while
for ϵ< 1
6 they are η =η0, 1−η0, where
(10) η0 = 1
2
(
1−
√
1− 6ϵ
1− 2ϵ
)
=ϵ + 3ϵ2+,...
Forη = 0;η∗ =ϵ>η . This, and the monotony and continuity of η∗ =fϵ(η) therefore
imply:
First case, ϵ≥ 1
6 : 0≤η <1
2 implies η <η∗< 1
2; 1
2 <η ≤ 1 implies 1
2 <η∗<η .
Second case, ϵ < 1
6 : 0 ≤ η < η0 implies η < η∗ < η0;η0 < η≤ 1
2 implies
η0 < η∗ < η; 1
2 < η <1−η0 implies η < η∗ < 1−η0; 1−η0 < η <1 implies
1−η0<η∗<η .
Now we must expect numerous successive occurrences of the situation under con-
sideration, if it is to be used as a basic procedure. Hence the iterative behavior of
the operation η→η∗ =fϵ(η) is relevant. Now it is clear from the above, that in the
ﬁrst case the successive iterates of the process in question always converge to 1
2, no
matter what the original η : while in the second case these iterates converge to η0 if
the original η <1
2, and to 1−η0 if the original η >1
2.
In other words: In the ﬁrst case no error level other than η∼ 1
2 can maintain
itself in the long run. I.e. the process asymptotically degenerates to total irrelevance,


<!-- PDF page 34 -->

26 Probabilistic Logics
like the one discussed in 7.1. In the second case the error-levels η∼η0 andη∼ 1−η0
will not only maintain themselves in the long run, but they represent the asymptotic
behavior for any original η <1
2 or η >1
2, respectively.
These arguments although heuristic, make it clear that the second case alone can
be used for the desired error-level control. I.e. we must require η < 1
6, i.e. the error-
level for a single basic organ function must be less than ∼ 16%. The stable, ultimate
error-level should then be η0 (we postulate, of course, that the start be made with an
error-levelη <1
2). η0 is small if ϵ is, hence ϵ must be small, and so
(11) η0 =ϵ + 3ϵ2 +...
This would therefore give an ultimate error-level of ∼ 10% (i.e. η∼ .1) for a single
basic organ function error-level of ∼ 8% (i.e. ϵ∼.08).
8.3.2 The rigorous argument.
To make this heuristic argument binding, it would be necessary to construct an error
controlling networkP∗ for any given networkP, so that all basic organs in it are so
connected as to put them into the special case of a majority organ, as discussed above.
This will not be uniformly possible, and it will therefore be necessary to modify the
above heuristic argument, although its general pattern will be maintained.
It is then desired to ﬁnd, for any given network P, an essentially equivalent
networkP∗, which is error-safe in some suitable sense, that conforms with the ideas
expressed so far. We will deﬁne this as meaning, that for each output line of P∗
(corresponding to one of (P), the (separate) probability of an incorrect message (over
this line) is≤η1. The value of η1 will result from the subsequent discussion.
The construction will be an induction over the longest serial chain of basic organs
inP, say µ =µ(P).
Consider the structure ofP. The number of its inputsi and outputsσ is arbitrary,
but every output of P must either come from a basic organ in P, or directly from
an input, or from a ground or live source. Omit the ﬁrst mentioned basic organs
fromP, as well as the outputs other than the ﬁrst mentioned ones, and designate
the network that is let over by Q. This is schematically shown in Figure 28. (Some
of the apparently separate outputs of Q may be split lines coming from a single one,
but this is irrelevant for what follows.)
IfQ is void, then there is nothing to prove; let therefore Q be non-void. Then
clearly µ(Q) =µ(P)− 1.
Hence the induction permits us to assume the existence of a network Q∗ which
is essentially equivalent toQ, and has for each output a (separate) error-probability
≤η1.
We now provide three copies of Q∗ :Q∗1,Q∗2,Q∗3, and constructQ∗ as shown
in Figure 29. (Instead of drawing the, rather complicated, connections across the
two dotted areas, they are indicated by attaching identical markings to endings that
should be connected.)


<!-- PDF page 35 -->

Control of Error in Single Line Automata 27
Now the (separate) output error-probabilities ofQ∗ are (by inductive assumption)
≤η1. The majority organs in the bottom row in Figure 29 (those without a ) are
so connected as to belong into the special case for a majority organ (cf. 8.2), hence
their outputs have (separate) error-probabilities≤fϵ(η1). The majority organs in the
top row in Figure 29 (those with a ) are in the general case, hence their (separate)
error-probabilities are≤ϵ + 3fϵ(η1).
Consequently the inductive step succeeds, and therefore the attempted inductive
proof is binding if
(12) ϵ + 3fϵ(η1)≤η1.


<!-- PDF page 36 -->

28 Probabilistic Logics


<!-- PDF page 37 -->

Control of Error in Single Line Automata 29
8.4 Numerical evaluation.
Substituting the expression (9) for fϵ(η) into condition (12) gives
4ϵ + 3(1− 2ϵ)(3η2
1− 2η3
1)≤η1,
i.e.
η3
1− 3
2η2
1 + 1
6(1− 2ϵ)η1− 2ϵ
3(1− 2ϵ)≥ 0.
Clearly the smallestη1> 0 fulﬁlling this condition is wanted. Since the left hand side
is < 0 for η1≥ 0, this means the smallest (real, and hence, by the above, positive)
root of
(13) η3
1− 3
2η2
1 + 1
6(1− 2ϵ)η1− 2ϵ
3(1− 2ϵ) = 0.
We know from the preceding heuristic argument, that ϵ≤ 1
6 will be necessary – but
actually even more must be required. Indeed, for η1 = 1
2 the left hand side of (13)
is =−(1 +ϵ)/(6− 12ϵ) < 0, hence a signiﬁcant and acceptable η1 (i.e. an η1 < 1
2),
can be obtained from (13) only if it has three real roots. A simple calculation shows,
that for ϵ = 1
6 only one real root exists η1 = 1.425. Hence the limiting ϵ calls for
the existence of a double root. Further calculation shows, that the double root in
question occurs for ϵ =.0073, and that its value isη1 =.060. Consequently ϵ<. 0073
is the actual requirement, i.e. the error-level of a single basic organ function must be
<. 73%. The stable, ultimate error-level is then the smallest positive root η1 of (13).
η1 is small if ϵ is, hence ϵ must be small, and so (from (13))
η1 = 4ϵ + 152ϵ2 +...
It is easily seen, that e.g. an ultimate error level of 2% (i.e. η1 =.02, calls for a single
basic organ function error-level of .41% (i.e. ϵ =.0041).
This result shows that errors can be controlled. But the method of construction
used in the proof about threefolds the number of basic organs in P∗ for an increase
of µ(P) by 1, hence P∗ has to contain about 3 µ(P) such organs. Consequently the
procedure is impractical.
The restriction ϵ < .0073 has no absolute signiﬁcance. It could be relaxed by
iterating the process of triplication at each step. The inequality ϵ < 1
6 is essential,
however, since our ﬁrst argument showed, that forϵ≥ 1
6 even for a basic organ in the
most favorable situation (namely in the “special” one) no interval of improvement
exists.


<!-- PDF page 38 -->

30 Probabilistic Logics
9. THE TECHNIQUE OF MULTIPLEXING.
9.1 General remarks on multiplexing.
The general process of multiplexing in order to control error was already referred to
in 7.4 (p. 22). The messages are carried on N lines. A positive number ∆( < 1
2) is
chosen and the stimulation of ≥ (1− ∆)N lines of the bundle is interpreted as a
positive message, the stimulation of ≤ δN lines as a negative message. Any other
number of stimulated lines is interpreted as malfunction. The complete system must
be organized in such a manner, that a malfunction of the whole automaton cannot
be caused by the malfunctioning of a single component, or of a small number of
components, but only by the malfunctioning of a large number of them. As we will
see later, the probability of such occurrences can be made arbitrarily small provided
the number of lines in each bundle is made suﬃciently great. All of Section 9 will be
devoted to a description of the method of constructing multiplexed automata and its
discussion, without considering the possibility of error in the basic components. In
Section 10 (p. 37) we will then introduce errors in the basic components, and estimate
their eﬀects.
9.2 The majority organ.
9.2.1 The basic executive organ.
The ﬁrst thing to consider is the method of constructing networks which will perform
the tasks of the basic organs for bundles of inputs and outputs instead of single lines.
A simple example will make the process clear: Consider the problem of construct-
ing the analogue of the majority organ which will accommodate bundles of ﬁve lines.
This is, easily done using the ordinary majority organ of Figure 14 (p. 13), as shown
in Figure 30. (The connections are replaced by suitable markings, in the same way
as in Figure 29 (p. 28)).


<!-- PDF page 39 -->

The Technique of Multiplexing 31
9.2.2 The need for a restoring organ.
It is intuitively clear that if almost all lines of the input bundles are stimulated, then
almost all lines of the output bundle will be stimulated. Similarly if almost none of the
lines of two of the input bundles are stimulated, then the mechanism will stimulate
almost none of its output lines. However, another fact is brought to light. Suppose
that a critical level ∆ = 1/5 is set for the bundles. Then if two of the input bundles
have 4 lines stimulated while the other has none, the output may have only 3 lines
stimulated. The same eﬀect prevails in the negative case. If two bundles have just
one input each stimulated, while the third bundle has all of its inputs stimulated,
then the resulting output may be the stimulation of two lines. In other words, the
relative number of lines in the bundle, which are not in the majority state, can double
in passing through the generalized majority system. A more careful analysis (similar
to the one that will be gone into in more detail for the case of the Scheﬀer organ in
Section 10 (p. 37)) shows the following: If, in some situation, the operation of the
organ should be governed by a two-to-one majority of the input bundles (i.e. if two
of the bundles are both prevalently stimulated or both prevalently non-stimulated,
while the third one is in the opposite condition), then the most probable level of
the output error will be (approximately) the sum of the errors in the two governing
input bundles; on the other hand in an operation in which the organ is governed
by a unanimous behavior of its input bundles (i.e. if all three of the bundles are
prevalently stimulated or all three are prevalently non-stimulated), then the output
error will generally be smaller than the (maximum of the) input errors. Thus in the
signiﬁcant case of two-to-one majorization, two signiﬁcant inputs may combine to
produce a result lying in the intermediate region of uncertain information. What is
needed therefore is a new type of organ which will restore the original stimulation
level. In other words, we need a network having the property that, with a fairly high
degree of probability, it transforms an input bundle with a stimulation level which
is near to zero or to one into an output bundle with stimulation level which is even
closer to the corresponding extreme.
Thus the multiplexed systems must contain two types of organs. The ﬁrst type is
the executive organ which performs the desired basic operations on the bundles. The
second type is an organ which restores the stimulation level of the bundles, and hence
erases the degradation caused by the executive organs. This situation has its analog
in many of the real automata which perform logically complicated tasks. For example
in electrical circuits, some of the vacuum tubes perform executive functions, such as
detection or rectiﬁcation or gating or coincidence-sensing, while the remainder are
assigned the task of ampliﬁcation, which is a restorative operation.
9.2.3 The restoring organ.
9.2.3.1 Construction.
The construction of a restoring organ is quite simple in principle, and in fact contained
in the second remark made in 9.2.2. In a crude way, the ordinary majority organ


<!-- PDF page 40 -->

32 Probabilistic Logics
already performs this task. Indeed in the simplest case, for a bundle of three lines, the
majority organ has precisely the right characteristics: It suppresses a single incoming
impulse as well as a single incoming non-impulse, i.e. it ampliﬁes the prevalence of
the presence as well as of the absence of impulses. To display this trait most clearly,
it suﬃces to split its output line into three lines, as shown in Figure 31.
Now for large bundles, in the sense of the remark referred to above, concerning
the reduction of errors in the case of a response induced by a unanimous behavior
of the input bundles, it is possible to connect up majority organs in parallel and
thereby produce the desired restoration. However, it is necessary to assume that the
stimulated (or non-stimulated) lines are distributed at random in the bundle. This
randomness must then be maintained at all times. The principle is illustrated by
Figure 32. The “black box” U is supposed to permute the lines of the input bundle
that pass through it, so as to restore the randomness of the pulses in its lines. This is
necessary, since to the left ofU the input bundle consists of a set of triads, where the
lines of each triad originate in the splitting of a single line, and hence are always all
three in the same condition. Yet, to the right ofU the lines of the corresponding triad
must be statistically independent, in order to permit the application of the statistical
formula to be given below for the functioning of the majority organ into which they
feed. The way to select such a “randomizing” permutation will not be considered
here – it is intuitively plausible that most “complicated” permutations will be suited
for this “randomizing” role. (cf. 11.2.)
9.2.3.2 Numerical evaluation.
If αN of theN incoming lines are stimulated, then the probability of any majority
organ being stimulated (by two or three stimulated inputs) is
(14) α∗ = 3α2− 2α3≡g(α).
Thus approximately (i.e. with high probability, provided N is large) α∗N outputs
will be excited. Plotting the curve of α∗ against α, as shown in Figure 33, indicates
clearly that this organ will have the desired characteristics:
This curve intersects the diagonalα∗ =α three times: For α = 0, 1
2, 1. 0 <α< 1
2
implies 0<α∗,α ; 1
2 <α< 1 impliesα<α ∗, 1. I.e. successive iterates of this process
converge to 0 if the original α< 1
2 and to 1 if the original α> 1
2.
In other words: The error levels α∼ 0 and α∼ 1 will not only maintain them-
selves in the long run but they represent the asymptotic behavior for any original
α < 1
2 or α > 1
2 respectively. Note, that because of g(1−α)≡ 1−g(α) there is
complete symmetry between the α< 1
2 region and the α> 1
2 region.


<!-- PDF page 41 -->

The Technique of Multiplexing 33
The process α→α∗ thus brings every α nearer to that one of 0 and 1 , to which
it was nearer originally. This is precisely that process of restoration, which was seen
in 9.2.2 to be necessary. I.e. one or more (successive) applications of this process will
have the required restoring eﬀect.
Note that this process of restoration is most eﬀective whenα−α∗ = 2α3−3α2+α
has its minimum or maximum, i.e. for
6α2− 6α + 1 = 0, i.e. forα = (3±
√
5)/6 =.788,. 212.
Thenα−α∗ =±.096. I.e. the maximum restoration is eﬀected on error levels at the
distance of 21.2% from 0% or 100% – these are improved (brought nearer) by 9 .6%.
9.3 Other basic organs.
We have so far assumed that the basic components of the construction are majority
organs. From these, an analogue of the majority organ – one which picked out a
majority of bundles instead of a majority of single lines – was constructed. Since
this, when viewed as a basic organ, is a universal organ, these considerations show
that it is at least theoretically possible to construct any network with bundles instead
of single lines. However there was no necessity for starting from majority organs.
Indeed, any other basic system whose universality was established in Section 4 can
be used instead. The simplest procedure in such a case is to construct an (essential)
equivalent of the (single line) majority organ from the given basic system (cf. 4.2.2
(p. 13)), and then proceed with this composite majority organ in the same way as
was done above with the basic majority organ.
Thus, if the basic organs are those Nos. one and two in Figure 10 (p. 10) (cf.
the relevant discussion in 4.1.2 (p. 9), then the basic synthesis (that of the majority
organ, cf. above) is immediately derivable from the introductory formula of Figure 14
(p. 13).


<!-- PDF page 42 -->

34 Probabilistic Logics
9.4 The Scheﬀer stroke.
9.4.1 The executive organ.
Similarly, it is possible to construct the entire,mechanism starting from the Scheﬀer
organ of Figure 12. In this case, however, it is simpler not to eﬀect the passage to
an (essential) equivalent of the majority organ (as suggested above), but to start de
novo. Actually, the same procedure, which was seen above to work for the majority
organ, works mutatis mutandis for the Scheﬀer organ, too. A brief description of the
direct procedure in this case is given in what follows:
Again, one begins by constructing a network which will perform the task of the
Scheﬀer organ for bundles of inputs and outputs instead of single lines. This is shown
in Figure 34 for bundles of ﬁve wires. (The connections are replaced by suitable
markings, as in Figure 29 and 30.)
It is intuitively clear that if almost all lines of both input bundles are stimulated,
then almost none of the lines of the output bundle will be stimulated. Similarly, if
almost none of the lines of one input bundle are stimulated, then almost all lines of
the output bundle will be stimulated. In addition to this overall behavior, the follow-
ing detailed behavior is found (cf. the detailed consideration in 10.4 (p. 42)). If the
condition of the organ is one of prevalent non-stimulation of the output bundle, and
hence is governed by (prevalent stimulation of) both input bundles, then the most
probable level of the output error will be (approximately) the sum of the errors in
the two governing input bundles; if on the other hand the condition of the organ is
one of prevalent stimulation of the output bundle, and hence is governed by (preva-
lent non-stimulation of) one or of both input bundles, then the output error will be
on (approximately) the same level as the input error, if (only) one input bundle is
governing (i.e. prevalently non-stimulated), and it will be generally smaller than the
input error, if both input bundles were governing (i.e. prevalently non-stimulated).
Thus two signiﬁcant inputs may produce a result lying in the intermediate zone of
uncertain information. Hence a restoring organ (for the error level) is again needed,
in addition to the executive organ.


<!-- PDF page 43 -->

The Technique of Multiplexing 35
9.4.2 The restoring organ.
Again the above indicates that the restoring organ can be obtained from a special
case functioning of the standard executive organ, namely by obtaining all inputs from
a single input bundle, and seeing to it that the output bundle has the same size as
the original input bundle. The principle is illustrated by Figure 35. “The black box”
U is again supposed to eﬀect a suitable permutation of the lines that pass through
it, for the same reasons and in the same manner as in the corresponding situation for
the majority organ (cf. Figure 32). I.e. it must have a “randomizing” eﬀect.
IfαN of theN incoming lines are stimulated, then the probability of any Scheﬀer
organ being stimulated (by at least one non-stimulated input) is
(15) α+ = 1−α2≡h(α).
Thus approximately (i.e. with high probability providedN is large)∼α+N outputs
will be excited. Plotting the curve, of α+ against α discloses some characteristic
diﬀerences against the previous case (that one of the majority organs, i.e. α∗ =
3α2− 2α3≡g(α), cf. 9.2.3), which require further discussion. This curve is shown in
Figure 36. Clearly α+ is an antimonotone function of α, i.e. instead of restoring an
excitation level (i.e. bringing it closer to 0 or to 1, respectively), it transforms it into
its opposite (i.e. it brings the neighborhood of 0 close to 1, and the neighborhood of
1 close to 0). In addition it produces for α near to 1 an α+ less near to 0 (about
twice farther), but for α near to 0 α+ much nearer to 1 (second order!). All these
circumstances suggest that the operation should be iterated.
Let the restoring organ therefore consist of two of the previously pictured organs
in series, as shown in Figure 37. (The “black boxes” U1,U2 play the same role as
their analogU plays in Figure 35.) This organ transforms an input excitation level
αN into an output excitation level of approximately (cf. above) ∼α++ where
α++ = 1− (1−α2)2≡h(h(α))≡k(α),
i.e.
(16) α++ = 2α2−α4≡k(α),
This curve of α++ againstα is shown in Figure 38. This curve is very similar to that
one obtained for the majority organ (i.e. α∗ = 3α2− 2α3≡g(α), (cf. 9.2.3). Indeed:
The curve intersects the diagonal α++ =α in the interval 0≤α++≤ 1 three times:
Forα = 0,α 0, 1, where α0 = (−1 +
√
5)/2 = .618. (There is a fourth intersection
α =−1−α0 =−1.618, but this is irrelevant, since it is not in the interval 0≤α≤ 1.)
0<α<α 0 implies 0 <α ++<α ; α0<α< 1 implies α<α ++< 1.


<!-- PDF page 44 -->

36 Probabilistic Logics


<!-- PDF page 45 -->

Error in Multiplex Systems 37
In other words: The role of the error levels α∼ 0 andα∼ 1 is precisely the same
as for the majority organ (cf. 9.2.3), except that the limit between their respective
areas of control lies at α =α0 instead of at α = 1
2. I.e. the process α→α++ brings
every α nearer to either 0 or to 1, but the preference to 0 or to 1, is settled at a
discrimination level of 61.8% (i.e.α0) instead of one of 50% (i.e. 1
2). Thus, apart from
a certain asymmetric distortion, the organ behaves like its counterpart considered for
the majority organ – i.e. is an eﬀective restoring mechanism.
10. ERROR IN MULTIPLEX SYSTEMS.
10.1 General remarks.
In Section 9 (p. 30) the technique for constructing multiplexed automata was de-
scribed. However the role of errors entered at best intuitively and summarily, and
therefore it has still not been proved that these systems will do what is claimed for
them – namely control error. Section 10 is devoted to a sketch of the statistical analy-
sis necessary to show that, by using large enough bundles of lines, any desired degree
of accuracy (i.e. as small a probability of malfunction of the ultimate output of the
network as desired) can be obtained with a multiplexed automaton.
For simplicity, we will only consider automata which are constructed from the
Scheﬀer organs. These are easier to analyze since they involve only two inputs. At
the same time, the Scheﬀer organ is (by itself) universal (cf. 4.2.1 (p. 12)), hence every
automaton is essentially equivalent to a network of Scheﬀer organs.
Errors in the operation of an automaton arise from two sources. First, the indi-
vidual basic organs can make mistakes. It will be assumed as before, that, under any
circumstance, the probability of this happening is justϵ. Any operation on the bundle
can be considered as a random sampling of size N (N being the size of the bundle).
The number of errors committed by the individual basic organs in any operation on
the bundle is then a random variable, distributed approximately normally with mean
ϵN and standard deviation
√
ϵ(1−ϵ)N . A second source of failures arises because
in operating with bundles which are not all in the same state of stimulation or non-
stimulation, the possibility of multiplying error by unfortunate combinations of lines
into the basic (single line) organs is always present. This interacts with the statisti-


<!-- PDF page 46 -->

38 Probabilistic Logics
cal eﬀects, and in particular with the processes of degeneration and of restoration of
which we spoke in 9.2.2, 9.2.3 and 9.4.2.
10.2 The distribution of the response set size.
10.2.1 Exact theory.
In order to give a statistical treatment of the problem, consider the Figure 34 (p. 34),
showing a network of Scheﬀer organs, which was discussed in 9.4.1. Let again N
be the number of lines in each (input or output) bundle. Let X be the set of those
i = 1,..., N for which line No. i in the ﬁrst input bundle is stimulated at time t; let
Y be the corresponding set for the second input bundle at time t; and let Z be the
corresponding set for the output bundle, assuming the correct functioning of all the
Scheﬀer organs involved, at timet + 1. LetX,Y haveξN,ηN elements, respectively,
but otherwise be random – i.e. equidistributed over all pairs of sets with these numbers
of elements. What can then be said about the number of elements ζN ofZ? Clearly
ξ,η,ζ are the relative levels of excitation of the two input bundles and of the output
bundle, respectively, of the network under consideration. The question is then: what
is the distribution of the (stochastic) variable ζ in terms of the (given) ξ,η ?
LetW be the complimentary set of Z. Let p,q,r be the numbers of elements of
X,Y,W, respectively, so that p =ξN,q =ηN,r = (1−ζ)N . Then the problem is
to determine the distribution of the (stochastic) variabler in terms of the (given)p,q
– i.e. the probability of any given r in combination with any given p,q .
W is clearly the intersection of the sets X,Y :W =X·Y . LetU,V be the (rel-
ative) complements of W inX,Y respectively: U =X−W ,V =Y−W , and let
S be the (absolute, i.e. in the set (1 ,..., N )) complement of the sum of X and
Y : S = −(X +Y). Then W,U,V,S are pairwise disjoint sets making up to-
gether precisely the entire set (1 ,..., N ), with r,p−r,q−r,N− p−q +r ele-
ments, respectively. Apart from this they are unrestricted. Thus they oﬀer together
N !/[r!(p−r)!(q−r)!(N− p−q +r)!] possible choices. Since there are a priori
N !/[p!(N− p)!] possible choices of anX withp elements and a prioriN !/[q!(N− q)!]
possible choices of aY withq elements, this means that the looked for probability of
W havingr elements is
ϱ =
( N !
r!(p−r)!(q−r)!(N− p−q +r)!
/ N !
p!(N− p)!
N !
q!(N− q)!
)
= p!(N− p)!q!(N− q)!
r!(p−r)!(q−r)!(N− p−q +r)!N !.
Note that this formula also shows thatϱ = 0 whenr< 0 orp−r< 0 orq−r< 0
orN− p−q +r< 0, i.e. when r violates the conditions
max(0,p +q−N )≤r≤ min(p,q ).


<!-- PDF page 47 -->

Error in Multiplex Systems 39
This is clear combinatorially, in view of the meaning of X,Y andW. In terms of
ξ,η,ζ the above conditions become
(17) 1 − max(0,ξ +η− 1)≥ζ≥ 1− min(ξ,η ).
Returning to the expression for ϱ, substituting the ξ,η,ζ expressions for p,q,r
and using Stirling’s formula for the factorials involved, gives
(18) ϱ∼ 1√
2πN
√αe−θN,
where
α = ξ(1−ζ)η(1−η)
(ζ +ξ− 1)(ζ +η− 1)(1−ζ)(2−ξ−η−ζ),
θ =(ζ +ξ− 1) ln(ζ +ξ− 1) + (ζ +η− 1) ln(ζ +η− 1)
+(1−ζ) ln(1−ζ) + (2−ξ−η−ζ) ln(2−ξ−η−ζ)
−ξ lnξ− (1−ξ) ln(1−ξ)−η lnη− (1−η) ln(1−η).
From this
∂θ
∂ζ = ln (ζ +ξ− 1)(ζ +η− 1)
(1−ζ)(2−ξ−η−ζ),
∂2θ
∂ζ 2 = 1
ζ +ξ− 1 + 1
ζ +η− 1 + 1
1−ζ + 1
2−ξ−η−ζ.
Hence θ = 0, ∂θ
∂ζ = 0 for ζ = 1−ξη, and ∂2θ
∂ζ 2 > 0 for all ζ (in its entire interval
of variability according to (17)). Consequently θ >0 for all ζ̸= 1−ξη (within the
interval (17)). This implies, in view of (18), that for all ζ which are signiﬁcantly
̸= 1−ξη, ϱtends to 0 very rapidly as N gets large. It suﬃces therefore to evaluate
(18) for ζ∼ 1−ξη. Now α = 1/[ξ(1−ξ)η(1−η)], ∂2θ
∂ζ 2 = 1/[ξ(1−ξ)η(1−η)] for
ζ = 1−ξη. Hence
α∼ 1
ξ(1−ξ)η(1−η),
θ∼ (ξ− (1−ξη))2
2ξ(1−ξ)η(1−η)
for ζ∼ 1−ξη. Therefore
(19) ϱ∼ 1√
2πξ(1−ξ)η(1−η)N
e− ζ−(1−ξη))2
2ξ(1−ξ)η(1−η)N
is an acceptable approximation for ϱ.
r is an integer-valued variable, henceζ = 1− r
N is a rational valued variable, with
the ﬁxed denominatorN . SinceN is assumed to be very large, the range of ζ is very
dense. It is therefore permissible to replace it by a continuous one, and to describe the
distribution of ζ by a probability-density σ. ϱ is the probability of a single value of


<!-- PDF page 48 -->

40 Probabilistic Logics
ζ, and since the values of ζ are equidistant, with a separation dζ = 1/N, the relation
betweenσ and ϱ is best deﬁned by σdζ =ϱ, i.e. σ =ϱN . Therefore (19) becomes
(20) σ∼ 1√
2π
√
ξ(1−ξ)η(1−η)/N
e
− 1
2
(
ζ−(1−ξη)√
ξ(1−ξ)η(1−η)/N
)2
.
This formula means obviously the following:
ζ is approximately normally distributed, with the mean 1 −ξη and the disper-
sion
√
ξ(1−ξ)η(1−η)/N . Note, that the rapid decrease of the normal distribu-
tion function (i.e. the right hand side of (20) with N (which is exponential!) is
valid as long as ζ is near to 1 −ξη, only the coeﬃcient of N (in the exponent, i.e.
− 1
2
(
[ζ− (1−ξη)]/
√
ξ(1−ξ)η(1−η)/N
)2
is somewhat altered as ζ deviates from
1−ξη. (This follows from the discussion of θ given above.)
The simple statistical discussion of 9.4 amounted to attributing to ζ the unique
value 1−ξη. We see now that this is approximately true:
(21)



ζ = (1−ξη) +
√
ξ(1−ξ)η(1−η)/Nδ,
δ is a stochastic variable, normally distributed, with mean 0
and dispersion 1.
10.2.2 Theory with errors.
We must now pass fromr,ζ, which postulate faultless functioning of all Scheﬀer organs
in the network, tor′,ζ′, which correspond to the actual functioning of all these organs
– i.e. to a probability ϵ of error on each functioning. Among the N− r organs each
of which should correctly stimulate its output, each error reduces r′ by one unit. The
number of errors here is approximately normally distributed, with the mean ϵr and
the dispersion
√
ϵ(1−ϵ)r (cf. the remark made in 10.1 (p. 37)). Among the N− r
organs, each of which should correctly not stimulate its output, each error increasesr′
by one unit. The number of errors here is again approximately normally distributed,
with the mean ϵ( N−r) and the dispersion
√
ϵ(1−ϵ)(N− r) (cf. as above). Thus
r′−r is the diﬀerence of these two (independent) stochastic variables. Hence it, too,
is approximately normally distributed, with the mean −ϵr +ϵ(N− r) =ϵ(N− 2r),
and the dispersion
√(√
ϵ(1−ϵ)r
)2
+
(√
ϵ(1−ϵ)(N− r
)2
=
√
ϵ(1−ϵ)N.
I.e. (approximately)
r′ =r + 2ϵ
(N
2 −r
)
+
√
ϵ(1−ϵ)N δ′,
where δ′ is normally distributed with the mean 0 and the dispersion 1. From this
ζ′ =ζ + 2ϵ
(1
2−ζ
)
+
√
ϵ(1−ϵ)N δ′,


<!-- PDF page 49 -->

Error in Multiplex Systems 41
and then by (21)
ζ′ =(1−ξη) + 2ϵ(ξη− 1
2)
+ (1− 2ϵ)
√
ξ(1−ξ)η(1−η)/N δ
−
√
ϵ(1−ϵ)/N.
Clearly (1−2ϵ)
√
ξ(1−ξ)η(1−η)/N δ−
√
ϵ(1−ϵ)/N δ′, too, is normally distributed,
with the mean 0 and the dispersion
√(
(1− 2ϵ)
√
ξ(1−ξ)η(1−η)/N
)2
+
(√
ϵ(1−ϵ)/N
)2
=
√(
(1− 2ϵ)2ξ(1−ξ)η(1−η) +ϵ(1−ϵ)
)/
N.
Hence (21) becomes at last (we write again ζ in place of ζ′):
(22)



ζ = (1 −ξη) + 2ϵ(ξη− 1
2)
+
√(
(1− 2ϵ)2ξ(1−ξ)η(1−η)
)/
N δ∗,
δ∗ is a stochastic variable, normally distributed, with
the mean 0 and the dispersion 1.
10.3 The restoring organ.
This discussion equally covers the situations that are dealt with in Figures 35 and 37
(p. 36), showing networks of Scheﬀer organs in 9.4.2 (p. 34).
Consider ﬁrst Figure 35. We have here a single input bundle of N lines, and
an output bundle of N lines. However, the two-way split and the subsequent “ran-
domizing” permutation produce an input bundle of 2N lines and (to the right of U)
the even lines of this bundle on one hand, and its odd lines on the other hand, may
be viewed as two input bundles of N lines each. Beyond this point the network is
the same as that one of Figure 34 (p. 34), discussed in 9.4.1 (p. 34). If the original
input bundle hadξN stimulated lines, then each one of the two derived input bundles
will also have ξN stimulated lines. (To be sure of this, it is necessary to choose the
“randomizing” permutationU of Figure 35 in such a manner, that it permutes the
even lines among each other, and the odd lines among each other. This is compatible
with its “randomizing” the relationship of the family of all even lines to the family of
all odd lines. Hence it is reasonable to expect that this requirement does not conﬂict
with the desired randomizing character of the permutation.) Let the output bundle
haveζN stimulated lines. Then we are clearly dealing with the same case as in (22),


<!-- PDF page 50 -->

42 Probabilistic Logics
except that it is specialized to ξ =η. Hence (22) becomes:
(23)



ζ = (1 −ξ2) + 2ϵ(ξ2− 1
2)
+
√(
(1− 2ϵ)2(ξ(1−ξ))2 +ϵ(1−ϵ)
)/
N δ∗
δ∗ is a stochastic variable, normally distributed, with the mean 0
and the dispersion 1.
Consider next Figure 37 (p. 36). Three bundles are relevant here: The input
bundle at the extreme left, the intermediate bundle issuing directly from the ﬁrst
tier of Scheﬀer organs, and the output bundle issuing directly from the second tier
of Scheﬀer organs, i.e. at the extreme right. Each one of these three bundles consists
ofN lines. Let the number of stimulated lines in each bundle be ζN,ωN,ψN,
respectively. Then (23) above applies, with its ξ,ζ replaced ﬁrst by ζ,ω, and second
byω,ψ :
(24)



ω = (1 −ζ2) + 2ϵ(ζ2− 1
2)
+
√(
(1− 2ϵ)2(ζ(1−ζ))2 +ϵ(1−ϵ)
)/
N δ∗∗,
ψ = (1 −ω2) + 2ϵ(ω2− 1
2)
+
√(
(1− 2ϵ)2(ω(1−ω))2 +ϵ(1−ϵ)
)/
N δ∗∗∗,
δ∗∗,δ∗∗∗ are stochastic variables, independently and normally
distributed, with the mean 0 and the dispersion 1.
10.4 Qualitative evaluation of the results.
In what follows, (22) and (24) will be relevant – i.e: the Scheﬀer organ networks of
Figures 34 and 37.
Before going into these considerations however, we have to make an observation
concerning (22). (22) shows that the (relative) excitation levels ξ,η on the input
bundles of its network generate approximately (i.e. for large N and small ϵ) the
(relative) excitation level ζ0 = 1−ξη on the output bundle of that network. This
justiﬁes the statements made in 9.4.1 about the detailed functioning of the network.
Indeed: if the two input bundles are both prevalently stimulated, i.e. if ξ∼ 1,η ∼ 1
then the distance of ζ0 from 0 is about the sum of the distances of ξ and ofη from 1 :
ζ0 = (1−ξ)+ξ(1−η). If one of the two input bundles, say the ﬁrst one, is prevalently
non-stimulated, while the other one is prevalently stimulated, i.e. ifξ∼ 0,η∼ 1, then
the distance of ζ0 from 1 is about the distance of ξ from 0 : 1 −ζ0 = ξη. If both
input bundles are prevalently non-stimulated, i.e. if ξ∼ 0,η ∼ 0, then the distance
ofζ0 from 1 is small compared to the distances of both ξ andη from 0 : 1−ζ0 =ξη.


<!-- PDF page 51 -->

Error in Multiplex Systems 43
10.5 Complete quantitative theory.
10.5.1 General results.
We can now pass to the complete statistical analysis of the Scheﬀer stroke operation
on bundles. In order to do this, we must agree on a systematic way to handle this
operation by a network. The system to be adopted will be the following: the necessary
executive organ will be followed in series by a restoring organ. I.e. the Scheﬀer organ
network of Figure 34 will be followed in series by the Scheﬀer organ network of Figure
37. This means that the formulas of (22) are to be followed by those of (24). Thus
ξ,η are the excitation levels of the two input bundles, ψ is the excitation level of the
output bundle, and we have:
(25)



ζ = (1−ξη) + 2ϵ(ζη− 1
2)
+
√(
(1− 2ϵ)2ξ(1−ξ)η(1−η) +ϵ(1−ϵ)
)/
N δ∗,
ω = (1−ζ2) + 2ϵ(ζ2− 1
2)
+
√
((1− 2ϵ)2(ζ(1−ζ))2 +ϵ(1−ϵ)/N δ∗∗,
ψ = (1−ω2) + 2ϵ(ω2− 1
2)
+
√(
(1− 2ϵ)2(ω(1−ω))2 +ϵ(1−ϵ)
)/
N δ∗∗∗,
δ∗, δ∗∗,δ∗∗∗ are stochastic variables, independently and normally
distributed, with the mean 0 and the dispersion 1.
Consider now a given ﬁduciary level ∆. Then we need a behavior, like the “cor-
rect” one of the Scheﬀer stroke, with an overwhelming probability. This means: the
implication of ψ≤ ∆ by ξ≥ 1− ∆,η ≥ 1− ∆; the implication of ψ≥ 1− ∆ by
ξ≤ ∆,η≥ 1− ∆; the implication of ψ≥ 1− ∆ byξ≤ ∆,η≤ ∆. (We are, of course,
using the symmetry in ξ,η .)
This may, of course, only be expected for N suﬃciently large and ϵ suﬃciently
small. In addition, it will be necessary to make an appropriate choice of the ﬁduciary
level ∆.
IfN is so large and ϵ is so small that all terms in (25) containing factors 1 /
√
N
andϵ can be neglected, then the above desired “overwhelmingly probable inferences”
become even strictly true, if ∆ is small enough. Indeed, then (25) gives ζ = ζ0 =
1−ξη, ω = ω0 = 1−ζ2, ψ = ψ0 = 1−ω2, i.e. ψ = 1− (2ξη− (ξη)2)2. Now
it is easy to verify ψ = O(∆2) for ξ ≥ 1− ∆,η ≥ 1− ∆;ψ = 1 −O(∆2) for
ξ≤ ∆,η ≥ 1− ∆;ψ = 1−O(∆4) for ξ≤ ∆,η ≤ ∆. Hence suﬃciently small ∆ will
guarantee the desiderata stated further above.
10.5.2 Numerical evaluation.
Consider next the case of a ﬁxed, ﬁnite N and a ﬁxed, positive ϵ. Then a more


<!-- PDF page 52 -->

44 Probabilistic Logics
elaborate calculation must be based on the complete formulæ of (25). This calculation
will not be carried out here, but its results will be described.
The most favorable ﬁduciary level ∆ , from the point of view of this calculation
turns out to be ∆ = .07. I.e. stimulation of at least 93% of the lines of a bundle
represents a positive message; stimulation of at most 7% of the lines of a bundle rep-
resents a negative message; the interval between 7% and 93% is a zone of uncertainty,
indicating an eﬀective malfunction of the network.
Having established this ﬁduciary level, there exists also an upper bound for the
allowable values of ϵ. This is ϵ = .0107. In other words if ϵ≥ .0107, the risk of
eﬀective malfunction of the network will be above a ﬁxed, positive lower bound, no
matter how large a bundle size N is used. The calculations were therefore continued
with a speciﬁc ϵ<. 0107, namely, withϵ =.005.
With these assumptions, then, the calculation yields an estimate for the probabil-
ity of malfunction of the network, i.e. of the violation of the desiderata stated further
above. As is to be expected, this estimate is given by an error integral. This is
(26)



ϱ(n) = 1√
2π
∫∞
κ e− 1
2x2
dx≈ 1√
2πκe− 1
2κ2
,
where
κ = .062
√
N
expresses, in a certain sense, the total allowable error divided by a composite standard
deviation. The approximation is of course valid only for large N . It can also be
written in the form
(27) ϱ(n)≈ 6.4√
N
10− 8.6N
10,000.
The following table gives a better idea of the dependency expressed by the formula:*
n = number of lines in a bundle p(n)= probability of malfunction
Original value Calculated from (26)
1,000 2.7 x 10-2 2.98 x 10-2
2,000 2.6 x 10-3 3.08 x 10-3
3,000 2.5 x 10-4 3.68 x 10-4
5,000 4.0 x 10-6 6.10 x 10-6
10,000 1.6 x 10-10 2.90 x 10-10
20,000 2.8 x 10-19 9.20 x 10-19
25,000 1.2 x 10-23 5.52 x 10-23
* ed: equation (27) is in error. The original values are shown in column 2, the
values calculated from equation (26) are shown in the last column. von Neumann
must have used some other approximation which he meant to express in equation
(27). In any case, he likely did the numerical calculations in his head in a minute or
two, and they are suﬃciently accurate for his purposes.


<!-- PDF page 53 -->

Error in Multiplex Systems 45
10.5.3 Examples.
10.5.3.1 First example.
To get an idea of the signiﬁcance of these sizes and the corresponding approximations,
consider the two following examples.
Consider ﬁrst a computing machine with 2500 vacuum tubes each of which is
actuated on the average once every 5 microseconds. Assume that a mean free path
of 8 hours between errors is desired. In this period of time there will have been
1
5× 2, 500× 8× 3, 600× 106 = 1.4× 1013 actuations, hence the above speciﬁcation
calls forδ∼ 1/[1.4× 1013] = 7× 10−14. According to the above table this calls for an
N between 10,000 and 20,000 – interpolating linearly on – 10 logδ givesN = 14, 000.
I.e. the system should be multiplexed 14,000 times.
It is characteristic for the steepness of statistical curves in this domain of large
numbers of events, that a 25 percent increase of N, i.e.N = 17, 500, gives (again by
interpolation) δ = 4.5× 10−17, i.e. a reliability which is 1,600 times better.
10.5.3.2 Second example.
Consider second a plausible quantitative picture for the functioning of the human
nervous system. The number of neurons involved is usually given as 10 10, but this
number may be somewhat low, also the synaptic end-bulbs and other possible au-
tonomous sub-units may increase it signiﬁcantly, perhaps a few hundred times. Let
us therefore use the ﬁgure 10 13 for the number of basic organs that are present. A
neuron may be actuated up to 200 times per second, but this is an abnormally high
rate of actuation. The average neuron will probably be actuated a good deal less fre-
quently, in the absence of better information 10 actuations per second may be taken
as an average ﬁgure of at least the right order. It is hard to tell what the mean free
path between errors should be. Let us take the view that errors properly deﬁned are
to be quite serious errors, and since they are not ordinarily observed, let us take a
mean free path which is long compared to an ordinary human life – say 10,000 years.
This means 1013×10, 000×31, 536, 000×10 = 3.2×1025 actuations, hence it calls for
δ∼ 1/(3.2× 1025) = 3.2× 10−26. According to the table this lies somewhat beyond
N = 25, 000 – extrapolating linearly on – 10 logδ givesN = 28, 000.
Note, that if this interpretation of the functioning of the human nervous system
were a valid one (for this cf. the remark of 11.1), the number of basic organs involved
would have to be reduced by a factor 28,000. This reduces the number of relevant
actuations and increases the value of the necessary δ by the same factor. I.e. δ =
9× 10−22, and henceN = 23, 000. The reduction of N is remarkably small – only
20%. This makes a reevaluation of the reduced N with the newN,δ unnecessary: in
fact the new factor, i.e. 23,000, givesδ = 7.4×10−22 and this with the approximation
used above, againN = 23, 000. (Actually the change of N is∼ 120, i.e. only 1/2%!)
Replacing the 10,000 years, used above rather arbitrarily, by 6 months, introduces
another factor 20,000, and therefore a change of about the same size as the above


<!-- PDF page 54 -->

46 Probabilistic Logics
one – now the value is easily seen to be N = 23, 000 (uncorrected) or N = 19, 000
(corrected).
10.6 Conclusions.
All this shows that the order of magnitude ofN is remarkably insensitive to variations
in the requirements, as long as these requirements are rather exacting ones, but not
wholly outside the range of our (industrial or natural) experience. Indeed, the N
obtained above were all∼ 20, 000, to within variations lying between -30% and +40%.
10.7 The general scheme of multiplexing.
This is an opportune place to summarize our results concerning multiplexing, i.e.
the Sections 9 and 10. Suppose it is desired to build a machine to perform the
logical function f(x,y,... ) with a given accuracy (probability of malfunction on the
ﬁnal result of the entire operation) η, using Scheﬀer neurons whose reliability (or
accuracy), i.e. probability of malfunction on a single operation) is ϵ. We assume
ϵ =.005. The procedure is then as follows.
First, design a networkR for this functionf(x,y,... ) as though the basic (Schef-
fer) organs had perfect accuracy. Second, estimate the maximum number of sin-
gle (perfect) Scheﬀer organ reactions (summed over all successive operations of all
the Scheﬀer organs actually involved) that occur in the network R in evaluating
f(x,y,... ) – say m such reactions. Put δ = η/m. Third, estimate the bundle size
N that is needed to give the multiplexed Scheﬀer organ-like network (cf. 10.5.2) an
error probability of at most δ. Fourth, replace each single line of the network R by
a bundle of size N , and each Scheﬀer neuron of the network R by the multiplexed
Scheﬀer organ network that goes with this N (cf. 10.5.1. (p. 43)) – this gives a net-
workQ(N ). A “yes” will then be transmitted by the stimulation of more than 93% of
the strands in a bundle, a “no” by the stimulation of less than 7%, and intermediate
values will signify the occurrence of an essential malfunction of the total system.
It should be noticed that this construction multiplies the number of lines by
N and the number of basic organs by 3 N . (In 10.5.3 we used a uniform factor of
multiplicationN . In view of the insensitivity of N to moderate changes in δ that we
observed in 10.5.3.2, this diﬀerence is irrelevant.) Our above considerations show that
the size ofN is∼ 20, 000 in all cases that interest us immediately. This implies that
such techniques are impractical for present technologies of componentry (although
this may perhaps not be true for certain conceivable technologies of the future), but
they are not necessarily unreasonable (at least not on grounds of size alone) for the
micro-componentry of the human nervous system.
Note that the conditions are signiﬁcantly less favorable for the non-multiplexing
procedure to control error described in Section 8 (p. 23). That process multiplied
the number of basic organs by 3 µ, µ being the number of consecutive steps (i.e.


<!-- PDF page 55 -->

General Comment on Digitalization and Multiplexing 47
basic organ actuations) from input to output, (cf. the end of 8.4). (In this way of
counting, iterative processes must be counted as many times as iterations occur.)
Thus for µ = 160, which is not an excessive “logical depth,” even for a conventional
calculation, 3160∼ 2× 1076, i.e. somewhat above the putative order of the number of
electrons in the universe. For µ = 200 (only 25% more!) then 3 200∼ 2.5× 1095, i.e.
1.2× 1019 times more – in view of the above this requires no comment.
11. GENERAL COMMENTS ON DIGITALIZATION
AND MULTIPLEXING.
11.1 Plausibility of various assumptions regarding the digital
vs. analog character of the nervous system.
Now we pass to some remarks of a more general character.
The question of the number of basic neurons required to build a multiplexed
automaton serves as an introduction for the ﬁrst remark. The above discussion shows
that the multiplexing technique is impractical on the level of present technology, but
quite practical for a perfect1y conceivable more advanced technology and for the
natural relay organs (neurons). I.e. it merely calls for a, not at all unnatural, micro-
componentry. It is therefore quite reasonable to ask speciﬁcally, whether it, or some
thing more or less like it, is a feature of the actually existing human (or rather animal)
nervous system.
The answer is not clear cut. The main trouble with the multiplexing systems, as
described in the preceding Section, is that they follow too slavishly a ﬁxed plan of
construction – and speciﬁcally one, that is inspired by the conventional procedures of
mathematics and mathematical logics. It is true that the animal nervous systems, too,
obey some rigid “architectural” patterns in their large-scale construction, and that
those varieties, which make one suspect a merely statistical design seem to occur only
in ﬁner detail and on the micro-level. (It is characteristic of this duality that most
investigators believe in the existence of overall laws of large-scale nerve-stimulation
and composite action that have only a statistical character, and yet occasionally a
single neuron is known to control a whole reﬂex-arc.) It is true, that our multiplexing
scheme, too, is rigid only in its large-scale pattern (the prototype network R, as a
pattern, and the general layout of the executive-plus-restoring organ, as discussed in
10.7 and in 10.5.1), while the “random” permutation “black boxes” (cf. the relevant
Figures 32, 35, 37 in 9.2.3 and 9.4.2) are typical of a “merely statistical design.” Yet
the nervous system seems to be somewhat more ﬂexibly designed. Also, its “digital”
(neural) operations are rather freely alternating with “analog” (humoral) processes in
their complete chains of causation. Finally the whole logical pattern of the nervous
system seems to deviate in certain important traits qualitatively and signiﬁcantly
from our ordinary mathematical and mathematical-logical modes of operation. The
pulse-trains that carry “quantitative” messages along the nerve ﬁbers do not seem


<!-- PDF page 56 -->

48 Probabilistic Logics
to be coded digital expressions (like a binary or a (Morse or binary coded) decimal
digitalization) of a number, but rather “analog” expressions of one, by way of their
pulse-density, or something similar – although much more than ordinary care should
be exercised in passing judgments in this ﬁeld, where we have so little factual infor-
mation. Also, the “logical depth” of our neural operations – i.e. the total number of
basic operations from (sensual) input to (memory) storage or (motor) output seems
to be much less than it would be in any human automaton (e.g. a computing ma-
chine) dealing with problems of anywhere nearly comparable complexity. Thus deep
diﬀerences in the basic organizational principles are probably present.
Some similarities, in addition to the one referred to above, are nevertheless un-
deniable. The nerves are bundles of ﬁbers – like our bundles. The nervous system
contains numerous “neural pools” whose function may well be that of organs devoted
to the restoring of excitation levels. (At least of the two (extreme) levels, e.g. one
near to 0 and one near to 1 , as in the case discussed in Section 9, especially in 9.2.2,
and 9.2.3, 9.4.2. Restoring one level only – by exciting or quenching or establishing
some intermediate stationary level – destroys rather than restores information, since
a system with a single stable state has a memory capacity 0 (cf. the deﬁnition given
in 5.2. (p. 15)). For systems which can stabilize (i.e. restore) more than two excitation
levels, cf. 12.6. (p. 55))
11.2 Remarks concerning the concept of a random
permutation.
The second remark on the subject of multiplexed systems concerns the problem (which
was so carefully sidestepped in Section 9) of maintaining randomness of stimulation.
For all statistical analyses, it is necessary to assume that this randomness exists. In
networks which allow feedback, however, when a pulse from an organ gets back to
the same organ at some later time, there is danger of strong statistical correlation.
Moreover without randomness, situations may arise where errors tend to be ampliﬁed
instead of canceled out. E.g. it is possible, that the machine remembers its mistakes,
so to speak, and thereafter perpetuates them. A simpliﬁed example of this eﬀect is
furnished by the elementary memory organ of Figure 16 (p. 14), or by a similar one,
based on the Scheﬀer stroke, shown in Figure 39. We will discuss the latter. This
system, provided it makes no mistakes, ﬁres on alternate moments of time. Thus
it has two possible states: Either it ﬁres at even times or at odd times. (For a
quantitative discussion of Figure 16, cf. 5.1. (p. 14)) However, once the mechanism
makes a mistake, i.e. if it fails to ﬁre at the right parity, or if it ﬁres at the wrong
parity, that error will be remembered, i.e. the parity is now lastingly altered, until
there occurs a new mistake. A single mistake thus destroys the memory of this
particular machine for all earlier events. In multiplex systems, single errors are not
necessarily disastrous: but without the “random” permutations introduced in Section
9, accumulated mistakes can be still dangerous.


<!-- PDF page 57 -->

General Comment on Digitalization and Multiplexing 49
To be more speciﬁc: consider the network shown in Figure 35 (p. 36), but without
the line-permuting “black box” U. If each output line is now fed back into its input
line (i.e. into the one with the same number from above), then pulses return to the
identical organ from which they started, and so the whole organ is in fact a sum of
separate organs according to Figure 39, and hence it is just as subject to error as
a single one of those organs acting independently. However, if a permutation of the
bundle is interposed as shown, in principle, by U in Figure 35, then the accuracy
of the system may be (statistically) improved. This is, of course, the trait which is
being looked for by the insertion ofU, i.e. of a “random” permutation in the sense of
Section 9. But how is it possible to perform a “random” permutation?
The problem is not immediately rigorously deﬁned. It is, however, quite proper to
reinterpret it as a problem that can be stated in a rigorous form, namely: it is desired
to ﬁnd one or more permutations which can be used in the “blackboxes” marked with
U orU1,U2 in the relevant Figures 35, 37, so that the essential statistical properties
that are asserted there are truly present. Let’s consider the simpler one of these
two, i.e. the multiplexed version of the simple memory organ of Figure 39 – i.e. a
speciﬁc embodiment of Figure 35. The discussion given in 10.3 (p. 41) shows that
it is desirable that the permutation U of Figure 35 permute the even lines among
each other, and the odd lines among each other. A possible rigorous variant of the
question that should now be asked is this.
Find a ﬁduciary level ∆ > 0 and a probability ϵ >0, such that for any η > 0
and any s = 1, 2,... there exists an N =N (η,s ) and a permutation U =U (N ),
satisfying the following requirement: assume that the probability of error in a single
operation of any given Scheﬀer organ is ϵ. Assume that at the time t all lines of the
above network are stimulated, or that all are not stimulated. Then the number of
lines stimulated at the time t +s will be≥ (1− ∆)N or≤ ∆N, respectively, with
a probability ≥ 1−δ. In addition N (η,s )≤ C ln(s/η) with a constant C (which
should not be excessively great).
Note, that the results of Section 10 make the surmise seem plausible, that ∆ =
.07,ϵ = .005 and C∼ 10, 000/[8.6× ln 10]∼ 500 are suitable choices for the above
purpose.
The following surmise concerning the nature of the permutationU (N ) has a certain
plausibility: letN = 2l. Consider the 2l complexes (d1,d 2,...,d l) (dλ = 0, 1, forλ =
1,...,l ). Let these correspond in some one to one way to the 2l integersi = 1,..., N :
(28) i⇔ (d1,d 2,...,d l)
Now let the mapping
(29) i→i′ =U (N )i


<!-- PDF page 58 -->

50 Probabilistic Logics
be induced, under the correspondence (28), by the mapping
(30) ( d1,d 2,...,d l)→ (dl,d 1,...,d l−1).
Obviously, the validity of our assertion is independent of the choice of the correspon-
dence (28). Now (30) does not change the parity of ∑l
λ=1dλ, hence the desideratum
thatU (N ) i.e. (29), should not change the parity of i (cf. above) is certainly fulﬁlled,
if the correspondence (28) is so chosen as to let i have the same parity as ∑l
λ=1dλ.
This is clearly possible, since on either side each parity occurs precisely 2 l−1 times.
ThisU (N ) should fulﬁll the above requirements.
11.3 Remarks concerning the simpliﬁed probability
assumption.
The third remark on multiplexed automata concerns the assumption made in deﬁning
the unreliability of an individual neuron. It was assumed that the probability of the
neuron failing to react correctly was a constant ϵ, independent of time and of all
previous inputs. This is an unrealistic assumption. For example, the probability
of failure for the Scheﬀer organ of Figure 12 (p. 11) may well be diﬀerent when the
inputs α and β are both stimulated, from the probability of failure when α and not
β is stimulated. In addition, these probabilities may change with previous history, or
simply with time and other environmental conditions. Also, they are quite likely to
be diﬀerent from neuron to neuron. Attacking the problem with these more realistic
assumptions means ﬁnding the domains of operability of individual neurons, ﬁnding
the intersection of these domains (even when drift with time is allowed) and ﬁnally
carrying out the statistical estimates for this far more complicated situation. This
will not be attempted here.
12. ANALOG POSSIBILITIES.
12.1 Further remarks concerning analog procedures.
There is no valid reason for thinking that the system which has been developed in
the past pages is the only or the best model of any existing nervous system or of any
potential error-safe computing machine or logical machine. Indeed, the form of our
model-system is due largely to the inﬂuence of the techniques developed for digital
computing and to the trends of the last sixty years in mathematical logics. Now,
speaking speciﬁcally of the human nervous system this is an enormous mechanism –
at least 10 6 times larger than any artifact with which we are familiar – and its activ-
ities are correspondingly varied and complex. Its duties include the interpretation of
external sensory stimuli, of reports of physical and chemical conditions, the control


<!-- PDF page 59 -->

Analog Possibilities 51
of motor activities and of internal chemical levels, the memory function with its very
complicated procedures for the transformation of and the search for information, and
of course, the continuous relaying of coded orders and of more or less quantitative
messages. It is possible to handle all these processes by digital methods (i.e. by using
numbers and expressing them in the binary system – or, with some additional cod-
ing tricks, in the decimal or some other system), and to process the digitalized, and
usually numericized, information by algebraical (i.e. basically arithmetical) methods.
This is probably the way how a human designer would at present approach such
a problem. It was pointed out in the discussion in 11.1. (p. 47), that the available
evidence, though scanty and inadequate, rather tends to indicate that the human
nervous system uses diﬀerent principles and procedures. Thus message pulse trains
seem to convey meaning by certain analogic traits (within the pulse notation – i.e.
this seems to be a mixed, part digital, part analog system), like the time density of
pulses in one line, correlations of the pulse time series between diﬀerent lines in a
bundle, etc.
Hence our multiplexed system might come to resemble the basic traits of the
human nervous system more closely if we attenuated its rigidly discrete and digital
character in some respects. The simplest step in this direction, which is rather directly
suggested by the above remarks about the human nervous system, would seem to be
this.
12.2 A possible analog procedure.
12.2.1 The set up.
In our prototype network R each line carries a “yes” (i.e. stimulation) or a “no”
(i.e. non-stimulation) message – these are interpreted as digits 1 and 0 , respectively.
Correspondingly, in the ﬁnal (multiplexed) network R(N ) (which is derived from
R) each bundle carries a “yes” = 1 (i.e. prevalent stimulation) or a “no” = 0 (i.e.
prevalent non-stimulation) message. Thus only two meaningful states, i.e. average
levels of excitation are allowed for a bundle – actually for one of these ξ∼ 1 and for
the other ξ∼ 0.
Now for large bundle sizesN the average excitation level, ξ, is an approximately
continuous quantity (in the interval 0 ≤ ξ ≤ 1) – the larger N , the better the
approximation. It is therefore not unreasonable to try to evolve a system in which ξ
is treated as a continuous quantity in 0≤ξ≤ 1. This means an analog procedure (or
rather, in the sense discussed above, a mixed, part digital, part analog procedure).
The possibility of developing such a system depends, of course, on ﬁnding suitable
algebraic procedures that ﬁt into it, and being able to assure its stability in the
mathematical sense (i.e. adequate precision) and in the logical sense (i.e. adequate
control of errors). To this subject we will now devote a few remarks.


<!-- PDF page 60 -->

52 Probabilistic Logics
12.2.2 The operations.
Consider a multiplex automaton of the type which has just been considered in 12.2.1,
with bundle sizeN . Let ξ denote the level of excitation of the bundle at any point,
that is, the relative number of excited lines. With this interpretation, the automaton
is a mechanism which performs certain numerical operations on a set of numbers to
give a new number (or numbers). This method of interpreting a computer has some
advantages, as well as some disadvantages in comparison with the digital, “all or
nothing,” interpretation. The conspicuous advantage is that such an interpretation
allows the machine to carry more information with fewer components than a corre-
sponding digital automaton. A second advantage is that it is very easy to construct
an automaton which will perform the elementary operations of arithmetics. (Or, to
be more precise: an adequate subset of these. Cf. the discussion in 12.3) For example,
givenξ and η it is possible to obtain 1
2(ξ +η) as shown in Figure 40. Similarly, it is
possible to obtain αξ + (1−α)η for any constantα with 0≤α≤ 1. (Of course, there
must be α =M/N,M = 0, 1,...,N, but this range for α is the same “approximate
continuum” as that one for ξ, hence we may treat the former as a continuum just
as properly as the latter.) We need only choose αN lines from the ﬁrst bundle and
combine them with (1−α)N lines from the second. To obtain the quantity 1 −ξη
requires the following set-up shown in Figure 41. Finally we can produce any constant
excitation level α (0≤α≤ 1), by originating a bundle so that αN lines come from
a live source and (1−α)N from ground.
12.3 Discussion of the algebraical calculus resulting from the
above operations.
Thus our present analog system can be used to build up a system of algebra where
the fundamental operations are
(31)



α
αξ + (1−α)η
1−ξη



{
(for any constant α in
0≤α≤ 1),
}


<!-- PDF page 61 -->

Analog Possibilities 53
All these are to be viewed as functions ofξ,η . They lead to a system, in which one can
operate freely with all those functionsf(ξ1,ξ 2,...,ξ k) of anyk variablesξ1,ξ 2,...,ξ k,
that the functions of (31) generate. I.e. with all functions that can be obtained by
any succession of the following processes:
(A) In the functions of (31) replace ξ,η by any variables ξi,ξj.
(B) In a function f(ξ∗
1,...,ξ ∗
l ), that has already been obtained, replace the vari-
ables f(ξ∗
1,...,ξ ∗
l ), by any functions g1(ξ1,...,ξ k),...,g l(ξ1,...,ξ l), respec-
tively, that have already been obtained.
To these, purely algebraical-combinatorial processes we add a properly analytical one,
which seems justiﬁed, since we have been dealing with approximative procedures,
anyway:
(C) If a sequence of functions fµ(ξ1,...,ξ k),µ = 1, 2,..., that have already been
obtained, converges uniformly (in the domain 0≤ξ1≤ 1,..., 0≤ξk≤ 1) for
µ→∞ to f(ξ1,...,ξ k), then form this f(ξ1,...,ξ k).
Note, that in order to have the freedom of operation as expressed by (A), (B), the
same “randomness” conditions must be postulated as in the corresponding parts of
Sections 9 and 10. Hence “randomizing” permutationsU must be interposed between
consecutive executive organs (i.e. those described above and reenumerated in (A)),
just as in the Sections referred to above.
In ordinary algebra the basic functions are diﬀerent ones, namely:
(32)



α
ξ +η
ξη



{
(for any constant α in
0≤α≤ 1),
}
It is easily seen that the system (31) can be generated (by (A), (B)) from the
system (32), while the reverse is not obvious (not even with (C) added). In fact (31)
is intrinsically more special than (32), i.e. the functions that (31) generates are fewer
than those that (32) generates (this is true for (A), (B), and also for (A), (B), (C))
– the former do not even include ξ +η. Indeed all functions of (31), i.e. of (A) based
on (31), have this property: If all variables lie in the interval 0 ≤ ξ≤ 1, then the
function, too, lies in that interval. This property is conserved under the applications
of (B), (C). On the other handξ+η does not possess this property – hence it cannot be
generated by (A), (B), (C) from (31). (Note that the above property of the functions
of (31), and of all those that they generate, is a quite natural one: They are all dealing
with excitation levels, and excitation levels must, by their nature, be numbers ξ with
0≤ξ≤ 1.)
In spite of this limitation, which seems to mark it as essentially narrower than
conventional algebra, the system of functions generated (by (A), (B), (C)) from (31) is
broad enough for all reasonable purposes. Indeed, it can be shown that the functions
so generated comprise precisely the following class of functions:
All functions f(ξ1,ξ 2,...,ξ k) which, as long as their variables ξ1,ξ 2,...,ξ k lie in
the interval 0≤ξ≤ 1, are continuous and have their value lying in that interval, too.
We will not give the proof here, it runs along quite conventional lines.


<!-- PDF page 62 -->

54 Probabilistic Logics
12.4 Limitations of this system.
This result makes it clear that the above analog system, i.e. the system of (31),
guarantees for numbers ξ with 0 ≤ ξ≤ 1, (i.e. for the numbers that it deals with,
namely excitation levels) the full freedom of algebra and of analysis.
In view of these facts, this analog system would seem to have clear superiority
over the digital one. Unfortunately, the diﬃculty of maintaining accuracy levels
counterbalances the advantages to a large extent. The accuracy can never be expected
to exceed 1/N . In other words, there is an intrinsic noise level of the order 1 /N, i.e.
for theN considered in 10.5.2 and 10.5.3 (up to∼ 20,000) at best 10−4. Moreover, in
its eﬀects on the operations of (31), this noise level rises from 1/N to 1/
√
N . (E.g. for
the operation 1−ξη, cf. the result (21) and the argument that leads to it.) With the
above assumptions, this is at best, ∼ 10−2, i.e. 1%! Hence after a moderate number
of operations the excitation levels are more likely to resemble a random sampling of
numbers than mathematics.
It should be emphasized, however, that this is not a conclusive argument that
the human nervous system does not utilize the analog system. As was pointed out
earlier, it is in fact known for at least some nervous processes that they are of an
analog nature, and that the explanation of this may, at least in part, lie in the fact
that the “logical depth” of the nervous network is quite shallow in some relevant
places. To be more speciﬁc: the number of synapses of neurons from the peripheral
sensory organs down the aﬀerent nerve ﬁbers, through the brain, back through the
eﬀerent nerves to the motor system may not be more than ∼ 10. Of course the
parallel complexity of the network of neurons is indisputable. “Depth” introduced by
feedback in the human brain may be overcome by some kind of self-stabilization. At
the same time, a good argument can be put up that the animal nervous system uses
analog methods (as they are interpreted above) only in the crudest way, accuracy
being a very minor consideration.
12.5 A plausible analog mechanism: Density modulation
by fatigue.
Two more remarks should be made at this point. The ﬁrst one deals with some
more speciﬁc aspects of the analog element in the organization and functioning of
the human nervous system. The second relates to the possibility of stabilizing the
precision level of the analog procedure that was outlined above.
This is the ﬁrst remark. As we have mentioned earlier, many neurons of the
nervous system transmit intensities (i.e. quantitative data) by analog methods, but,
in a way entirely diﬀerent from the method described in 12.2, 12.3 and 12.4 (p. 51-
54). Instead of the level of excitation of a nerve (i.e. of a bundle of nerve ﬁbers)
varying, as described in 12.2, the single nerve ﬁbers ﬁre repetitiously, but with varying
frequency in time. For example, the nerves transmitting a pressure stimulus may vary
in frequency between, say, 6 ﬁrings per second and, say, 60 ﬁrings per second. This


<!-- PDF page 63 -->

Analog Possibilities 55
frequency is a monotone function of the pressure. Another example is the optic
nerve, where a certain set of ﬁbers responds in a similar manner to the intensity of
the incoming light. This kind of behavior is explained by the mechanism of neuron
operation, and in particular with the phenomena of threshold and of fatigue. With
any peripheral neuron at any time can be associated a threshold intensity: A stimulus
will make the neuron ﬁre if and only if its magnitude exceeds the threshold intensity.
The behavior of the threshold intensity as a function of the time after a typical
neuron ﬁres is qualitatively pictured in Figure 42. After ﬁring, there is an “absolute
refractory period” of about 5 milliseconds, during which no stimulus can make the
neuron ﬁre again. During this period, the threshold value is inﬁnite. Next comes a
“relative refractory period” of about 10 milliseconds, during which time the threshold
level drops back to its equilibrium value (it may even oscillate about this value a few
times at the end). This decrease is for the most part monotonic. Now the nerve
will ﬁre again as soon as it is stimulated with an intensity greater than its excitation
threshold. Thus if the neuron is subjected to continual excitation of constant intensity
(above the equilibrium intensity), it will ﬁre periodically with a period between 5 and
15 milliseconds, depending on the intensity of the stimulus.
Another interesting example of a nerve network which transmits intensity by
this means is the human acoustic system. The ear analyzes a sound wave into its
component frequencies. These are transmitted to the brain through diﬀerent nerve
ﬁbers with the intensity variations of the corresponding component represented by
the frequency modulation of nerve ﬁring.
The chief purpose of all this discussion of nervous systems is to point up the
fact that it is dangerous to identify the real physical (or biological) world with the
models which are constructed to explain it. The problem of understanding the animal
nervous action is far deeper than the problem of understanding the mechanism of a
computing machine. Even plausible explanations of nervous reaction should be taken
with a very large grain of salt.


<!-- PDF page 64 -->

56 Probabilistic Logics
12.6 Stabilization of the analog system.
We now come to the second remark. It was pointed out earlier, that the analog
mechanism that we discussed may have a way of stabilizing excitation levels to a
certain precision for its computing operations. This can be done in the following way.
For the digital computer, the problem was to stabilize the excitation level at (or
near) the two values 0 and 1. This was accomplished by repeatedly passing the bundle
through a simple mechanism which changed an excitation level ξ into the level f(ξ)
where the function f(ξ) had the general form shown in Figure 43. The reason that
such a mechanism is a restoring organ for the excitation levels ζ ∼ 0 and ξ ∼ 1
(i.e. that it stabilizes at – or near – 0 and 1) is that f(ξ) has this property: For
some suitable β(0≤ β≤ 1) 0 < ξ < βimplies 0 < f(ξ) < ξ ; β < ξ <1 implies
ξ <f(ξ)< 1. Thus ξ = 0, 1 are the only stable ﬁxpoints of f(ξ). (Cf. the discussion
in 9.2.3 and 9.4.2.)


<!-- PDF page 65 -->

Concluding Remark 57
Now consider another f(ξ) which has the form shown in Figure 44.
I.e. we have:
0 =α0<β 1<α 1<...<α ν−1<β ν <α ν = 1,
for i = 1,...,ν : αi−1<ξ <βi implies αi−1<f (ξ)<ξ,
βi<ξ <αi implies ξ <f(ξ)<α i.
Here α0(= 0),α 1,...,α ν−1,αν(= 1) are f(ξ)’s only stable ﬁxpoints, and such a
mechanism is a restoring organ for the excitation levels ξ∼ α0(= 0),α 1,...,α ν−1,
αν(= 1). Choose, e.g. αi = i/ν (i = 0, 1,...,ν ), with ν−1 < β, or more generally,
just αi−αi−1 < δ (i = 1,...,ν ) with some suitable ν. Then this restoring organ
clearly conserves precisions of the order δ (with the same prevalent probability with
which it restores).
13. CONCLUDING REMARK.
13.1 A possible neurological interpretation.
There remains the question, whether such a mechanism is possible with the means
that we are now envisaging. We have seen further above that this is the case, if a
function f(ξ) with the properties just described can be generated from (31). Such
a function can indeed be so generated. Indeed, this follows immediately from the
general characterization of the class of functions that can be generated from (31),
discussed in 12.3 (p. 52). However, we will not go here into this matter any further.
It is not inconceivable that some “neural pools” in the human nervous system
may be such restoring organs, to maintain accuracy in those parts of the network
where the analog principle is used, and where there is enough “logical depth” (cf.
12.4 (p. 54)) to make this type of stabilization necessary.


<!-- PDF page 66 -->

58 Probabilistic Logics
References
[1] S. C. Kleene, “Representation of Events in Nerve Nets and Finite Automata,”
RAND Research Memorandum RM 704 (The RAND Corp., 1500 Fourth St.,
Santa Monica, Calif.) Dec. 1951.
[2] W. S. McCulloch and W. Pitts, “A logical calculus of the ideas imminent in
nervous activity,” Bull. of Math. Biophysics, 5 (l943), p. 115-133.
[3] C. E. Shannon, “A Mathematical theory of communication,” The Bell System
Tech. Jour., 27(1948), p. 379-423.
[4] L. Szilard, “ ¨Uber die Entropieverminderung in einem thermodynamischen System
bei Eingriﬀen intelligenter Wesen,” Zeitschrift f¨ ur Physik, 53(1929), p. 840-856.
[5] A. M. Turing “On computable numbers,” Proc. of the London Math. Soc. 2-
42(1937), p. 230-265.
