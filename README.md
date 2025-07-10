# Instructions

1. Create a `.env` file containing the required varibles.
3. The `spiderTask2A.ipynb` file, run in google colab.
4. On a successful run, you will get a `vdb` folder in your google drive.
5. Download and save the folder locally and run the `app.py` file on local device.
6. From there, it will create and host a local server and you can ask it questions. :)

# Logs for some questions

### Q1. What is the main innovation introduced in the "Attention is All You Need" paper?

Answer : The main innovation introduced in the "Attention is All You Need" paper is scaled dot-product attention, multi-head attention and the parameter-free position representation.

#### Retrieved docs with cosine-similarities: 

##### Similarity :  0.5115201040317792 for the doc :

[Tur20] Project Turing. Microsoft research blog, Feb 2020.
[VBL+16] Oriol Vinyals, Charles Blundell, Timothy Lillicrap, Daan Wierstra, et al. Matching Networks for One
Shot Learning. In Advances in neural information processing systems, pages 3630–3638, 2016.
[VSP+17] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,Łukasz
Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in neural information processing
systems, 2017.
[WPN+19] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. Superglue: A stickier benchmark for general-purpose language understand-
ing systems. In Advances in Neural Information Processing Systems, pages 3261–3275, 2019.
[WXH+18] Yiren Wang, Yingce Xia, Tianyu He, Fei Tian, Tao Qin, ChengXiang Zhai, and Tie-Yan Liu. Multi-agent
dual learning. ICLR 2019, 2018.
[XDH+19] Qizhe Xie, Zihang Dai, Eduard Hovy, Minh-Thang Luong, and Quoc V . Le. Unsupervised data
augmentation for consistency training, 2019.
[YdC+19] Dani Yogatama, Cyprien de Masson d’Autume, Jerome Connor, Tomas Kocisky, Mike Chrzanowski,

##### Similarity :  0.4985134494585829  for the doc :  

has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head
attention and the parameter-free position representation and became the other person involved in nearly every
detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and
tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and
efﬁcient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and
implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating
our research.
†Work performed while at Google Brain.
‡Work performed while at Google Research.
31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.
Recurrent models typically factor computation along the symbol positions of the input and output
sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden
states ht, as a function of the previous hidden state ht−1 and the input for position t. This inherently

##### Similarity :  0.48738519086757887  For the doc :  

of synthetic tasks.
Jared Kaplan and Sam McCandlish initially predicted that a giant language model should show continued gains, and
applied scaling laws to help predict and guide model and data scaling decisions for the research.
Ben Mann implemented sampling without replacement during training.
Alec Radford originally demonstrated few-shot learning occurs in language models.
Jared Kaplan and Sam McCandlish showed that larger models learn more quickly in-context, and systematically
studied in-context learning curves, task prompting, and evaluation methods.
Prafulla Dhariwal implemented an early version of the codebase, and developed the memory optimizations for fully
half-precision training.
Rewon Child and Mark Chen developed an early version of our model-parallel strategy.
Rewon Child and Scott Gray contributed the sparse transformer.
Aditya Ramesh experimented with loss scaling strategies for pretraining.
Melanie Subbiah and Arvind Neelakantan implemented, experimented with, and tested beam search.
Pranav Shyam worked on SuperGLUE and assisted with connections to few-shot learning and meta-learning literature.

