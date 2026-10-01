/* ============================================================
   CURRICULUM — single source of truth for the whole site.
   The sidebar, landing page map, progress bar, and prev/next
   pager are all generated from this object. To add a lesson,
   add an entry here and create its HTML file in /lessons.
   ============================================================ */

const CURRICULUM = {
  title: "AI &amp; ML Mastery",
  subtitle: "From a number in a vector to a thinking machine",
  source: "Rebuilt from the IITM Pravartak — Advanced Certificate Programme in Applied AI &amp; ML",

  parts: [
    {
      id: "start",
      emoji: "🚀",
      title: "Start Here",
      blurb: "What this whole journey is about, and the one mental model that ties all 40 weeks together.",
      lessons: [
        { id: "w01", n: "1",  title: "The Big Picture: What is AI, really?", file: "lessons/w01.html", dur: "20 min", tags: ["overview", "intuition"] },
      ]
    },
    {
      id: "math",
      emoji: "📐",
      title: "Part 1 · Mathematical Foundations",
      blurb: "The three languages machines think in: linear algebra (space), calculus (change), and probability (uncertainty).",
      lessons: [
        { id: "w02", n: "2", title: "Linear Algebra: Vectors, Matrices &amp; Eigen-everything", file: "lessons/w02.html", dur: "60 min", tags: ["vectors", "matrices", "eigen", "SVD"] },
        { id: "w03", n: "3", title: "Calculus: Derivatives &amp; Optimisation", file: "lessons/w03.html", dur: "55 min", tags: ["derivatives", "gradients", "optimisation"] },
        { id: "w04", n: "4", title: "Probability: Reasoning Under Uncertainty", file: "lessons/w04.html", dur: "55 min", tags: ["random variables", "Gaussian", "expectation"] },
      ]
    },
    {
      id: "data",
      emoji: "🐍",
      title: "Part 2 · Data &amp; Python",
      blurb: "How we store data (SQL), how we wrangle it (Python), and how we listen to it before modelling (EDA).",
      lessons: [
        { id: "w05", n: "5", title: "SQL &amp; Databases: Where Data Lives", file: "lessons/w05.html", dur: "50 min", tags: ["SQL", "RDBMS", "NoSQL"] },
        { id: "w06", n: "6", title: "Python I: Fundamentals &amp; Data Structures", file: "lessons/w06.html", dur: "50 min", tags: ["python", "lists", "dicts", "functions"] },
        { id: "w07", n: "7", title: "Python II: NumPy, Generators, Decorators &amp; Scaling", file: "lessons/w07.html", dur: "55 min", tags: ["numpy", "generators", "decorators"] },
        { id: "w08", n: "8", title: "Exploratory Data Analysis (EDA)", file: "lessons/w08.html", dur: "50 min", tags: ["statistics", "cleaning", "visualisation"] },
      ]
    },
    {
      id: "apps",
      emoji: "🌐",
      title: "Part 3 · The Worlds of AI",
      blurb: "A guided tour of what AI actually does with text, images, video and audio — the problems before the algorithms.",
      lessons: [
        { id: "w09", n: "9",  title: "NLP &amp; Text Processing", file: "lessons/w09.html", dur: "45 min", tags: ["NLP", "tokenisation"] },
        { id: "w10", n: "10", title: "Image, Video &amp; Audio Processing", file: "lessons/w10.html", dur: "45 min", tags: ["vision", "audio", "signals"] },
      ]
    },
    {
      id: "classical",
      emoji: "🧮",
      title: "Part 4 · Classical Machine Learning",
      blurb: "Learning from data without neural networks: regression, classification, SVMs, dimensionality reduction, trees, ensembles and clustering.",
      lessons: [
        { id: "w11", n: "11", title: "Paradigms of ML I: Supervised &amp; Unsupervised", file: "lessons/w11.html", dur: "45 min", tags: ["supervised", "unsupervised"] },
        { id: "w12", n: "12", title: "Paradigms of ML II: Self-supervised, Online, Meta &amp; RL", file: "lessons/w12.html", dur: "45 min", tags: ["self-supervised", "meta", "RL"] },
        { id: "w13", n: "13", title: "Regression I: Linear &amp; Multiple Linear Regression", file: "lessons/w13.html", dur: "55 min", tags: ["regression", "least squares"] },
        { id: "w14", n: "14", title: "Regression II: Nonlinear, Overfitting &amp; Regularisation", file: "lessons/w14.html", dur: "55 min", tags: ["polynomial", "overfitting", "ridge"] },
        { id: "w15", n: "15", title: "Classification I: k-NN &amp; Evaluating Classifiers", file: "lessons/w15.html", dur: "55 min", tags: ["kNN", "precision", "recall", "ROC"] },
        { id: "w16", n: "16", title: "Classification II: Bayes, Naïve Bayes &amp; GMM", file: "lessons/w16.html", dur: "60 min", tags: ["bayes", "MLE", "GMM"] },
        { id: "w17", n: "17", title: "SVM I: Discriminant Functions &amp; the Perceptron", file: "lessons/w17.html", dur: "50 min", tags: ["perceptron", "discriminant"] },
        { id: "w18", n: "18", title: "SVM II: Margins, Kernels &amp; the Kernel Trick", file: "lessons/w18.html", dur: "60 min", tags: ["SVM", "margin", "kernel"] },
        { id: "w19", n: "19", title: "Dimensionality Reduction I: Normalisation &amp; Data Reduction", file: "lessons/w19.html", dur: "45 min", tags: ["normalisation", "z-score"] },
        { id: "w20", n: "20", title: "Dimensionality Reduction II: PCA &amp; Fisher LDA", file: "lessons/w20.html", dur: "55 min", tags: ["PCA", "LDA", "eigen"] },
        { id: "w21", n: "21", title: "Decision Trees &amp; CART", file: "lessons/w21.html", dur: "50 min", tags: ["trees", "entropy", "gini"] },
        { id: "w22", n: "22", title: "Ensemble Methods: Random Forests &amp; Boosting", file: "lessons/w22.html", dur: "50 min", tags: ["bagging", "random forest", "adaboost"] },
        { id: "w23", n: "23", title: "Clustering: k-Means &amp; Hierarchical", file: "lessons/w23.html", dur: "50 min", tags: ["k-means", "hierarchical"] },
      ]
    },
    {
      id: "deep",
      emoji: "🧠",
      title: "Part 5 · Deep Learning",
      blurb: "Neural networks from a single neuron to deep CNNs and RNNs — and the backpropagation algorithm that makes them learn.",
      lessons: [
        { id: "w24", n: "24", title: "Neural Networks I: Neurons &amp; Activation Functions", file: "lessons/w24.html", dur: "55 min", tags: ["perceptron", "activation", "softmax"] },
        { id: "w25", n: "25", title: "Neural Networks II: Backpropagation", file: "lessons/w25.html", dur: "60 min", tags: ["backprop", "gradient descent", "logistic"] },
        { id: "w26", n: "26", title: "Deep FFN I: Gradient Descent &amp; Adaptive Optimisers", file: "lessons/w26.html", dur: "55 min", tags: ["SGD", "Adam", "regularisation"] },
        { id: "w27", n: "27", title: "Deep FFN II: Dropout &amp; Batch Normalisation", file: "lessons/w27.html", dur: "45 min", tags: ["dropout", "batchnorm"] },
        { id: "w28", n: "28", title: "CNNs I: Convolution &amp; Pooling", file: "lessons/w28.html", dur: "60 min", tags: ["convolution", "pooling", "CNN"] },
        { id: "w29", n: "29", title: "CNNs II: ResNets, Transfer Learning &amp; Segmentation", file: "lessons/w29.html", dur: "55 min", tags: ["resnet", "transfer learning"] },
        { id: "w30", n: "30", title: "RNNs I: Sequences, LSTM &amp; GRU", file: "lessons/w30.html", dur: "60 min", tags: ["RNN", "LSTM", "GRU"] },
        { id: "w31", n: "31", title: "RNNs II: Seq2Seq &amp; Word Embeddings", file: "lessons/w31.html", dur: "60 min", tags: ["seq2seq", "word2vec", "embeddings"] },
      ]
    },
    {
      id: "modern",
      emoji: "✨",
      title: "Part 6 · Transformers &amp; Generative AI",
      blurb: "The architecture behind ChatGPT. Attention, transformers, LLMs, RAG, and generative models (GANs).",
      lessons: [
        { id: "w32", n: "32", title: "Transformers I: Self-Attention &amp; Multi-Head Attention", file: "lessons/w32.html", dur: "70 min", tags: ["attention", "transformer"] },
        { id: "w33", n: "33", title: "Transformers II: Positional Encoding &amp; Pre-training", file: "lessons/w33.html", dur: "55 min", tags: ["positional encoding", "BERT", "pretraining"] },
        { id: "w34", n: "34", title: "Transformers III: LLMs, Multimodal &amp; RAG", file: "lessons/w34.html", dur: "60 min", tags: ["LLM", "RAG", "multimodal"] },
        { id: "w35", n: "35", title: "GANs I: The Generator–Discriminator Game", file: "lessons/w35.html", dur: "55 min", tags: ["GAN", "generator", "discriminator"] },
        { id: "w36", n: "36", title: "GANs II: Conditional, Image-to-Image &amp; Text-to-Image", file: "lessons/w36.html", dur: "50 min", tags: ["cGAN", "pix2pix", "cycleGAN"] },
        { id: "w37", n: "37", title: "Applications of Generative AI", file: "lessons/w37.html", dur: "45 min", tags: ["genai", "diffusion", "text-gen"] },
      ]
    },
    {
      id: "prod",
      emoji: "⚙️",
      title: "Part 7 · Production &amp; Reinforcement Learning",
      blurb: "Taking models out of the notebook: MLOps, cloud deployment, and learning by trial-and-error.",
      lessons: [
        { id: "w38", n: "38", title: "MLOps: Deploying &amp; Maintaining Models", file: "lessons/w38.html", dur: "50 min", tags: ["mlops", "mlflow", "responsible AI"] },
        { id: "w39", n: "39", title: "Cloud Deployment: Containers, Serverless &amp; the Edge", file: "lessons/w39.html", dur: "50 min", tags: ["cloud", "docker", "serverless"] },
        { id: "w40", n: "40", title: "Reinforcement Learning: MDPs &amp; Learning to Act", file: "lessons/w40.html", dur: "55 min", tags: ["RL", "MDP", "rewards"] },
      ]
    },
  ],

  projects: [
    { id: "p1", n: "1", emoji: "📊", title: "The Tabular ML Pipeline", file: "projects/p1.html",
      blurb: "End-to-end: load data → EDA → train regression, trees, ensembles → reduce dimensions with PCA → cluster. Uses Parts 1–4.",
      uses: ["EDA", "Regression", "Decision Trees", "Random Forest", "PCA", "k-Means"] },
    { id: "p2", n: "2", emoji: "💬", title: "Sentiment &amp; Spam: A Text Classifier", file: "projects/p2.html",
      blurb: "Turn words into vectors, build a Naïve Bayes + neural classifier, evaluate with precision/recall. Uses Parts 3–5.",
      uses: ["NLP", "Naïve Bayes", "Embeddings", "Neural Nets", "Evaluation"] },
    { id: "p3", n: "3", emoji: "🖼️", title: "Image Classifier with CNNs &amp; Transfer Learning", file: "projects/p3.html",
      blurb: "Build a CNN from scratch, then fine-tune a pre-trained ResNet to recognise images. Uses Part 5.",
      uses: ["CNN", "Convolution", "Transfer Learning", "Training loops"] },
    { id: "p4", n: "4", emoji: "🤖", title: "Mini-GPT: Build a Language Model from Scratch", file: "projects/p4.html",
      blurb: "The crown jewel — go from embeddings to self-attention to a working transformer that generates text. Ties vectors → LLMs.",
      uses: ["Embeddings", "Self-Attention", "Transformer", "Training", "Generation"] },
    { id: "p5", n: "5", emoji: "☁️", title: "Ship It: Deploy a Model + RAG Chatbot to the Cloud", file: "projects/p5.html",
      blurb: "Wrap a model in an API, add a RAG layer, containerise and deploy with monitoring. Uses Parts 6–7.",
      uses: ["MLOps", "RAG", "Docker", "Cloud", "APIs"] },
    { id: "p6", n: "6", emoji: "🏥", title: "Hospital Risk Intelligence I: Data Foundations", file: "projects/p6.html",
      blurb: "Applied MLOps capstone, part I. SQL → EDA → feature engineering on a real-shaped 3-table hospital schema, with two genuine data bugs found along the way. Uses Parts 2 &amp; 4.",
      uses: ["SQL", "EDA", "Feature Engineering", "Data Quality", "Time-based split"] },
    { id: "p7", n: "7", emoji: "🏥", title: "Hospital Risk Intelligence II: Models, API &amp; Monitoring", file: "projects/p7.html",
      blurb: "Applied MLOps capstone, part II. Train Random Forest + Gradient Boosting, evaluate honestly, ship a validated FastAPI service, and catch a real drift false-alarm with PSI. Uses Parts 4 &amp; 7.",
      uses: ["Random Forest", "Gradient Boosting", "FastAPI", "Drift (PSI)", "Fairness", "MLOps"] },
    { id: "p8", n: "8", emoji: "✈️", title: "Wheels Up I: Private Aviation Data Foundations", file: "projects/p8.html",
      blurb: "The Project 6 spine, applied from scratch to a private-aviation customers/reservations/billing business. Uses Parts 2 &amp; 4.",
      uses: ["SQL", "EDA", "Feature Engineering", "Data Quality"] },
    { id: "p9", n: "9", emoji: "✈️", title: "Wheels Up II: Models, API &amp; Monitoring", file: "projects/p9.html",
      blurb: "The Project 7 spine on the aviation dataset — including a real, severe fairness gap on the highest-value customer segment. Uses Parts 4 &amp; 7.",
      uses: ["Random Forest", "Gradient Boosting", "FastAPI", "Drift (PSI)", "Fairness", "MLOps"] },
  ]
};

/* Flattened, ordered list of every lesson (for prev/next + progress). */
const ALL_LESSONS = CURRICULUM.parts.flatMap(p => p.lessons.map(l => ({ ...l, partId: p.id })));
const TOTAL_LESSONS = ALL_LESSONS.length;
