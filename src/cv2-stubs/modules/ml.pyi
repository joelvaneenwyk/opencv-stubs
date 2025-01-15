import builtins
from typing import Any, Final, overload, TypeAlias

from .. import functions as cv2

outputs: TypeAlias = Any
svidx: TypeAlias = Any
neighborResponses: TypeAlias = Any
covs: TypeAlias = Any
resp: TypeAlias = Any
probs: TypeAlias = Any
outputProbs: TypeAlias = Any
dist: TypeAlias = Any
alpha: TypeAlias = Any
labels: TypeAlias = Any
results: TypeAlias = Any
logLikelihoods: TypeAlias = Any
retval: TypeAlias = Any

class ANN_MLP(StatModel):
    def getAnnealCoolingRatio(self) -> retval:
        r"""
        @see setAnnealCoolingRatio
        """

    def getAnnealFinalT(self) -> retval:
        r"""
        @see setAnnealFinalT
        """

    def getAnnealInitialT(self) -> retval:
        r"""
        @see setAnnealInitialT
        """

    def getAnnealItePerStep(self) -> retval:
        r"""
        @see setAnnealItePerStep
        """

    def getBackpropMomentumScale(self) -> retval:
        r"""
        @see setBackpropMomentumScale
        """

    def getBackpropWeightScale(self) -> retval:
        r"""
        @see setBackpropWeightScale
        """

    def getLayerSizes(self) -> retval:
        r"""
        Integer vector specifying the number of neurons in each layer including the input and output layers.
        The very first element specifies the number of elements in the input layer.
        The last element - number of elements in the output layer.
        @sa setLayerSizes
        """

    def getRpropDW0(self) -> retval:
        r"""
        @see setRpropDW0
        """

    def getRpropDWMax(self) -> retval:
        r"""
        @see setRpropDWMax
        """

    def getRpropDWMin(self) -> retval:
        r"""
        @see setRpropDWMin
        """

    def getRpropDWMinus(self) -> retval:
        r"""
        @see setRpropDWMinus
        """

    def getRpropDWPlus(self) -> retval:
        r"""
        @see setRpropDWPlus
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getTrainMethod(self) -> retval:
        r"""
        Returns current training method
        """

    def getWeights(self, layerIdx) -> retval:
        r""""""

    def setActivationFunction(self, type, param1=..., param2=...) -> None:
        r"""
        Initialize the activation function for each neuron.
        Currently the default and the only fully supported activation function is ANN_MLP::SIGMOID_SYM.
        @param type The type of activation function. See ANN_MLP::ActivationFunctions.
        @param param1 The first parameter of the activation function, \f$\alpha\f$. Default value is 0.
        @param param2 The second parameter of the activation function, \f$\beta\f$. Default value is 0.
        """

    def setAnnealCoolingRatio(self, val) -> None:
        r"""
        @copybrief getAnnealCoolingRatio @see getAnnealCoolingRatio
        """

    def setAnnealFinalT(self, val) -> None:
        r"""
        @copybrief getAnnealFinalT @see getAnnealFinalT
        """

    def setAnnealInitialT(self, val) -> None:
        r"""
        @copybrief getAnnealInitialT @see getAnnealInitialT
        """

    def setAnnealItePerStep(self, val) -> None:
        r"""
        @copybrief getAnnealItePerStep @see getAnnealItePerStep
        """

    def setBackpropMomentumScale(self, val) -> None:
        r"""
        @copybrief getBackpropMomentumScale @see getBackpropMomentumScale
        """

    def setBackpropWeightScale(self, val) -> None:
        r"""
        @copybrief getBackpropWeightScale @see getBackpropWeightScale
        """

    def setLayerSizes(self, _layer_sizes) -> None:
        r"""
        Integer vector specifying the number of neurons in each layer including the input and output layers.
        The very first element specifies the number of elements in the input layer.
        The last element - number of elements in the output layer. Default value is empty Mat.
        @sa getLayerSizes
        """

    def setRpropDW0(self, val) -> None:
        r"""
        @copybrief getRpropDW0 @see getRpropDW0
        """

    def setRpropDWMax(self, val) -> None:
        r"""
        @copybrief getRpropDWMax @see getRpropDWMax
        """

    def setRpropDWMin(self, val) -> None:
        r"""
        @copybrief getRpropDWMin @see getRpropDWMin
        """

    def setRpropDWMinus(self, val) -> None:
        r"""
        @copybrief getRpropDWMinus @see getRpropDWMinus
        """

    def setRpropDWPlus(self, val) -> None:
        r"""
        @copybrief getRpropDWPlus @see getRpropDWPlus
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def setTrainMethod(self, method, param1=..., param2=...) -> None:
        r"""
        Sets training method and common parameters.
        @param method Default value is ANN_MLP::RPROP. See ANN_MLP::TrainingMethods.
        @param param1 passed to setRpropDW0 for ANN_MLP::RPROP and to setBackpropWeightScale for ANN_MLP::BACKPROP and to initialT for ANN_MLP::ANNEAL.
        @param param2 passed to setRpropDWMin for ANN_MLP::RPROP and to setBackpropMomentumScale for ANN_MLP::BACKPROP and to finalT for ANN_MLP::ANNEAL.
        """

    def create(self) -> retval:
        r"""
        @brief Creates empty model

        Use StatModel::train to train the model, Algorithm::load\<ANN_MLP\>(filename) to load the pre-trained model.
        Note that the train method has optional flags: ANN_MLP::TrainFlags.
        """

    def load(self, filepath) -> retval:
        r"""
        @brief Loads and creates a serialized ANN from a file
        *
        * Use ANN::save to serialize and store an ANN to disk.
        * Load the ANN from this file again, by calling this function with the path to the file.
        *
        * @param filepath path to serialized ANN
        """

class Boost(DTrees):
    def getBoostType(self) -> retval:
        r"""
        @see setBoostType
        """

    def getWeakCount(self) -> retval:
        r"""
        @see setWeakCount
        """

    def getWeightTrimRate(self) -> retval:
        r"""
        @see setWeightTrimRate
        """

    def setBoostType(self, val) -> None:
        r"""
        @copybrief getBoostType @see getBoostType
        """

    def setWeakCount(self, val) -> None:
        r"""
        @copybrief getWeakCount @see getWeakCount
        """

    def setWeightTrimRate(self, val) -> None:
        r"""
        @copybrief getWeightTrimRate @see getWeightTrimRate
        """

    def create(self) -> retval:
        r"""
        Creates the empty model.
        Use StatModel::train to train the model, Algorithm::load\<Boost\>(filename) to load the pre-trained model.
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized Boost from a file
        *
        * Use Boost::save to serialize and store an RTree to disk.
        * Load the Boost from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized Boost
        * @param nodeName name of node containing the classifier
        """

class DTrees(StatModel):
    def getCVFolds(self) -> retval:
        r"""
        @see setCVFolds
        """

    def getMaxCategories(self) -> retval:
        r"""
        @see setMaxCategories
        """

    def getMaxDepth(self) -> retval:
        r"""
        @see setMaxDepth
        """

    def getMinSampleCount(self) -> retval:
        r"""
        @see setMinSampleCount
        """

    def getPriors(self) -> retval:
        r"""
        @see setPriors
        """

    def getRegressionAccuracy(self) -> retval:
        r"""
        @see setRegressionAccuracy
        """

    def getTruncatePrunedTree(self) -> retval:
        r"""
        @see setTruncatePrunedTree
        """

    def getUse1SERule(self) -> retval:
        r"""
        @see setUse1SERule
        """

    def getUseSurrogates(self) -> retval:
        r"""
        @see setUseSurrogates
        """

    def setCVFolds(self, val) -> None:
        r"""
        @copybrief getCVFolds @see getCVFolds
        """

    def setMaxCategories(self, val) -> None:
        r"""
        @copybrief getMaxCategories @see getMaxCategories
        """

    def setMaxDepth(self, val) -> None:
        r"""
        @copybrief getMaxDepth @see getMaxDepth
        """

    def setMinSampleCount(self, val) -> None:
        r"""
        @copybrief getMinSampleCount @see getMinSampleCount
        """

    def setPriors(self, val) -> None:
        r"""
        @copybrief getPriors @see getPriors
        """

    def setRegressionAccuracy(self, val) -> None:
        r"""
        @copybrief getRegressionAccuracy @see getRegressionAccuracy
        """

    def setTruncatePrunedTree(self, val) -> None:
        r"""
        @copybrief getTruncatePrunedTree @see getTruncatePrunedTree
        """

    def setUse1SERule(self, val) -> None:
        r"""
        @copybrief getUse1SERule @see getUse1SERule
        """

    def setUseSurrogates(self, val) -> None:
        r"""
        @copybrief getUseSurrogates @see getUseSurrogates
        """

    def create(self) -> retval:
        r"""
        @brief Creates the empty model

        The static method creates empty decision tree with the specified parameters. It should be then
        trained using train method (see StatModel::train). Alternatively, you can load the model from
        file using Algorithm::load\<DTrees\>(filename).
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized DTrees from a file
        *
        * Use DTree::save to serialize and store an DTree to disk.
        * Load the DTree from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized DTree
        * @param nodeName name of node containing the classifier
        """

class EM(StatModel):
    def getClustersNumber(self) -> retval:
        r"""
        @see setClustersNumber
        """

    def getCovarianceMatrixType(self) -> retval:
        r"""
        @see setCovarianceMatrixType
        """

    def getCovs(self, covs=...) -> covs:
        r"""
        @brief Returns covariation matrices

        Returns vector of covariation matrices. Number of matrices is the number of gaussian mixtures,
        each matrix is a square floating-point matrix NxN, where N is the space dimensionality.
        """

    def getMeans(self) -> retval:
        r"""
        @brief Returns the cluster centers (means of the Gaussian mixture)

        Returns matrix with the number of rows equal to the number of mixtures and number of columns
        equal to the space dimensionality.
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getWeights(self) -> retval:
        r"""
        @brief Returns weights of the mixtures

        Returns vector with the number of elements equal to the number of mixtures.
        """

    def predict(self, samples, results=..., flags=...) -> tuple[retval, results]:
        r"""
        @brief Returns posterior probabilities for the provided samples

        @param samples The input samples, floating-point matrix
        @param results The optional output \f$ nSamples \times nClusters\f$ matrix of results. It contains posterior probabilities for each sample from the input
        @param flags This parameter will be ignored
        """

    def predict2(self, sample, probs=...) -> tuple[retval, probs]:
        r"""
        @brief Returns a likelihood logarithm value and an index of the most probable mixture component
        for the given sample.

        @param sample A sample for classification. It should be a one-channel matrix of \f$1 \times dims\f$ or \f$dims \times 1\f$ size.
        @param probs Optional output matrix that contains posterior probabilities of each component given the sample. It has \f$1 \times nclusters\f$ size and CV_64FC1 type.  The method returns a two-element double vector. Zero element is a likelihood logarithm value for the sample. First element is an index of the most probable mixture component for the given sample.
        """

    def setClustersNumber(self, val) -> None:
        r"""
        @copybrief getClustersNumber @see getClustersNumber
        """

    def setCovarianceMatrixType(self, val) -> None:
        r"""
        @copybrief getCovarianceMatrixType @see getCovarianceMatrixType
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def trainE(self, samples, means0, covs0=..., weights0=..., logLikelihoods=..., labels=..., probs=...) -> tuple[retval, logLikelihoods, labels, probs]:
        r"""
        @brief Estimate the Gaussian mixture parameters from a samples set.

        This variation starts with Expectation step. You need to provide initial means \f$a_k\f$ of
        mixture components. Optionally you can pass initial weights \f$\pi_k\f$ and covariance matrices
        \f$S_k\f$ of mixture components.

        @param samples Samples from which the Gaussian mixture model will be estimated. It should be a one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type it will be converted to the inner matrix of such type for the further computing.
        @param means0 Initial means \f$a_k\f$ of mixture components. It is a one-channel matrix of \f$nclusters \times dims\f$ size. If the matrix does not have CV_64F type it will be converted to the inner matrix of such type for the further computing.
        @param covs0 The vector of initial covariance matrices \f$S_k\f$ of mixture components. Each of covariance matrices is a one-channel matrix of \f$dims \times dims\f$ size. If the matrices do not have CV_64F type they will be converted to the inner matrices of such type for the further computing.
        @param weights0 Initial weights \f$\pi_k\f$ of mixture components. It should be a one-channel floating-point matrix with \f$1 \times nclusters\f$ or \f$nclusters \times 1\f$ size.
        @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        @param labels The optional output "class label" for each sample: \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        @param probs The optional output matrix that contains posterior probabilities of each Gaussian mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and CV_64FC1 type.
        """

    def trainEM(self, samples, logLikelihoods=..., labels=..., probs=...) -> tuple[retval, logLikelihoods, labels, probs]:
        r"""
        @brief Estimate the Gaussian mixture parameters from a samples set.

        This variation starts with Expectation step. Initial values of the model parameters will be
        estimated by the k-means algorithm.

        Unlike many of the ML models, %EM is an unsupervised learning algorithm and it does not take
        responses (class labels or function values) as input. Instead, it computes the *Maximum
        Likelihood Estimate* of the Gaussian mixture parameters from an input sample set, stores all the
        parameters inside the structure: \f$p_{i,k}\f$ in probs, \f$a_k\f$ in means , \f$S_k\f$ in
        covs[k], \f$\pi_k\f$ in weights , and optionally computes the output "class label" for each
        sample: \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most
        probable mixture component for each sample).

        The trained model can be used further for prediction, just like any other classifier. The
        trained model is similar to the NormalBayesClassifier.

        @param samples Samples from which the Gaussian mixture model will be estimated. It should be a one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type it will be converted to the inner matrix of such type for the further computing.
        @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        @param labels The optional output "class label" for each sample: \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        @param probs The optional output matrix that contains posterior probabilities of each Gaussian mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and CV_64FC1 type.
        """

    def trainM(self, samples, probs0, logLikelihoods=..., labels=..., probs=...) -> tuple[retval, logLikelihoods, labels, probs]:
        r"""
        @brief Estimate the Gaussian mixture parameters from a samples set.

        This variation starts with Maximization step. You need to provide initial probabilities
        \f$p_{i,k}\f$ to use this option.

        @param samples Samples from which the Gaussian mixture model will be estimated. It should be a one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type it will be converted to the inner matrix of such type for the further computing.
        @param probs0 the probabilities
        @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        @param labels The optional output "class label" for each sample: \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        @param probs The optional output matrix that contains posterior probabilities of each Gaussian mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and CV_64FC1 type.
        """

    def create(self) -> retval:
        r"""
        Creates empty %EM model.
        The model should be trained then using StatModel::train(traindata, flags) method. Alternatively, you
        can use one of the EM::train\* methods or load it from file using Algorithm::load\<EM\>(filename).
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized EM from a file
        *
        * Use EM::save to serialize and store an EM to disk.
        * Load the EM from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized EM
        * @param nodeName name of node containing the classifier
        """

class KNearest(StatModel):
    def findNearest(self, samples, k, results=..., neighborResponses=..., dist=...) -> tuple[retval, results, neighborResponses, dist]:
        r"""
        @brief Finds the neighbors and predicts responses for input vectors.

        @param samples Input samples stored by rows. It is a single-precision floating-point matrix of `<number_of_samples> * k` size.
        @param k Number of used nearest neighbors. Should be greater than 1.
        @param results Vector with results of prediction (regression or classification) for each input sample. It is a single-precision floating-point vector with `<number_of_samples>` elements.
        @param neighborResponses Optional output values for corresponding neighbors. It is a single- precision floating-point matrix of `<number_of_samples> * k` size.
        @param dist Optional output distances from the input vectors to the corresponding neighbors. It is a single-precision floating-point matrix of `<number_of_samples> * k` size.  For each input vector (a row of the matrix samples), the method finds the k nearest neighbors. In case of regression, the predicted result is a mean value of the particular vector's neighbor responses. In case of classification, the class is determined by voting.  For each input vector, the neighbors are sorted by their distances to the vector.  In case of C++ interface you can use output pointers to empty matrices and the function will allocate memory itself.  If only a single input vector is passed, all output matrices are optional and the predicted value is returned by the method.  The function is parallelized with the TBB library.
        """

    def getAlgorithmType(self) -> retval:
        r"""
        @see setAlgorithmType
        """

    def getDefaultK(self) -> retval:
        r"""
        @see setDefaultK
        """

    def getEmax(self) -> retval:
        r"""
        @see setEmax
        """

    def getIsClassifier(self) -> retval:
        r"""
        @see setIsClassifier
        """

    def setAlgorithmType(self, val) -> None:
        r"""
        @copybrief getAlgorithmType @see getAlgorithmType
        """

    def setDefaultK(self, val) -> None:
        r"""
        @copybrief getDefaultK @see getDefaultK
        """

    def setEmax(self, val) -> None:
        r"""
        @copybrief getEmax @see getEmax
        """

    def setIsClassifier(self, val) -> None:
        r"""
        @copybrief getIsClassifier @see getIsClassifier
        """

    def create(self) -> retval:
        r"""
        @brief Creates the empty model

        The static method creates empty %KNearest classifier. It should be then trained using StatModel::train method.
        """

    def load(self, filepath) -> retval:
        r"""
        @brief Loads and creates a serialized knearest from a file
        *
        * Use KNearest::save to serialize and store an KNearest to disk.
        * Load the KNearest from this file again, by calling this function with the path to the file.
        *
        * @param filepath path to serialized KNearest
        """

class LogisticRegression(StatModel):
    def getIterations(self) -> retval:
        r"""
        @see setIterations
        """

    def getLearningRate(self) -> retval:
        r"""
        @see setLearningRate
        """

    def getMiniBatchSize(self) -> retval:
        r"""
        @see setMiniBatchSize
        """

    def getRegularization(self) -> retval:
        r"""
        @see setRegularization
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getTrainMethod(self) -> retval:
        r"""
        @see setTrainMethod
        """

    def get_learnt_thetas(self) -> retval:
        r"""
        @brief This function returns the trained parameters arranged across rows.

        For a two class classification problem, it returns a row matrix. It returns learnt parameters of
        the Logistic Regression as a matrix of type CV_32F.
        """

    def predict(self, samples, results=..., flags=...) -> tuple[retval, results]:
        r"""
        @brief Predicts responses for input samples and returns a float type.

        @param samples The input data for the prediction algorithm. Matrix [m x n], where each row contains variables (features) of one object being classified. Should have data type CV_32F.
        @param results Predicted labels as a column matrix of type CV_32S.
        @param flags Not used.
        """

    def setIterations(self, val) -> None:
        r"""
        @copybrief getIterations @see getIterations
        """

    def setLearningRate(self, val) -> None:
        r"""
        @copybrief getLearningRate @see getLearningRate
        """

    def setMiniBatchSize(self, val) -> None:
        r"""
        @copybrief getMiniBatchSize @see getMiniBatchSize
        """

    def setRegularization(self, val) -> None:
        r"""
        @copybrief getRegularization @see getRegularization
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def setTrainMethod(self, val) -> None:
        r"""
        @copybrief getTrainMethod @see getTrainMethod
        """

    def create(self) -> retval:
        r"""
        @brief Creates empty model.

        Creates Logistic Regression model with parameters given.
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized LogisticRegression from a file
        *
        * Use LogisticRegression::save to serialize and store an LogisticRegression to disk.
        * Load the LogisticRegression from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized LogisticRegression
        * @param nodeName name of node containing the classifier
        """

class NormalBayesClassifier(StatModel):
    def predictProb(self, inputs, outputs=..., outputProbs=..., flags=...) -> tuple[retval, outputs, outputProbs]:
        r"""
        @brief Predicts the response for sample(s).

        The method estimates the most probable classes for input vectors. Input vectors (one or more)
        are stored as rows of the matrix inputs. In case of multiple input vectors, there should be one
        output vector outputs. The predicted class for a single input vector is returned by the method.
        The vector outputProbs contains the output probabilities corresponding to each element of
        result.
        """

    def create(self) -> retval:
        r"""
        Creates empty model
        Use StatModel::train to train the model after creation.
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized NormalBayesClassifier from a file
        *
        * Use NormalBayesClassifier::save to serialize and store an NormalBayesClassifier to disk.
        * Load the NormalBayesClassifier from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized NormalBayesClassifier
        * @param nodeName name of node containing the classifier
        """

class ParamGrid(builtins.object):
    def create(self, minVal=..., maxVal=..., logstep=...) -> retval:
        r"""
        @brief Creates a ParamGrid Ptr that can be given to the %SVM::trainAuto method

        @param minVal minimum value of the parameter grid
        @param maxVal maximum value of the parameter grid
        @param logstep Logarithmic step for iterating the statmodel parameter
        """

class RTrees(DTrees):
    def getActiveVarCount(self) -> retval:
        r"""
        @see setActiveVarCount
        """

    def getCalculateVarImportance(self) -> retval:
        r"""
        @see setCalculateVarImportance
        """

    def getOOBError(self) -> retval:
        r"""
        Returns the OOB error value, computed at the training stage when calcOOBError is set to true.
        * If this flag was set to false, 0 is returned. The OOB error is also scaled by sample weighting.
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getVarImportance(self) -> retval:
        r"""
        Returns the variable importance array.
        The method returns the variable importance vector, computed at the training stage when
        CalculateVarImportance is set to true. If this flag was set to false, the empty matrix is
        returned.
        """

    def getVotes(self, samples, flags, results=...) -> results:
        r"""
        Returns the result of each individual tree in the forest.
        In case the model is a regression problem, the method will return each of the trees'
        results for each of the sample cases. If the model is a classifier, it will return
        a Mat with samples + 1 rows, where the first row gives the class number and the
        following rows return the votes each class had for each sample.
        @param samples Array containing the samples for which votes will be calculated.
        @param results Array where the result of the calculation will be written.
        @param flags Flags for defining the type of RTrees.
        """

    def setActiveVarCount(self, val) -> None:
        r"""
        @copybrief getActiveVarCount @see getActiveVarCount
        """

    def setCalculateVarImportance(self, val) -> None:
        r"""
        @copybrief getCalculateVarImportance @see getCalculateVarImportance
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def create(self) -> retval:
        r"""
        Creates the empty model.
        Use StatModel::train to train the model, StatModel::train to create and train the model,
        Algorithm::load to load the pre-trained model.
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized RTree from a file
        *
        * Use RTree::save to serialize and store an RTree to disk.
        * Load the RTree from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized RTree
        * @param nodeName name of node containing the classifier
        """

class SVM(StatModel):
    def getC(self) -> retval:
        r"""
        @see setC
        """

    def getClassWeights(self) -> retval:
        r"""
        @see setClassWeights
        """

    def getCoef0(self) -> retval:
        r"""
        @see setCoef0
        """

    def getDecisionFunction(self, i, alpha=..., svidx=...) -> tuple[retval, alpha, svidx]:
        r"""
        @brief Retrieves the decision function

        @param i the index of the decision function. If the problem solved is regression, 1-class or 2-class classification, then there will be just one decision function and the index should always be 0. Otherwise, in the case of N-class classification, there will be \f$N(N-1)/2\f$ decision functions.
        @param alpha the optional output vector for weights, corresponding to different support vectors. In the case of linear %SVM all the alpha's will be 1's.
        @param svidx the optional output vector of indices of support vectors within the matrix of support vectors (which can be retrieved by SVM::getSupportVectors). In the case of linear %SVM each decision function consists of a single "compressed" support vector.  The method returns rho parameter of the decision function, a scalar subtracted from the weighted sum of kernel responses.
        """

    def getDegree(self) -> retval:
        r"""
        @see setDegree
        """

    def getGamma(self) -> retval:
        r"""
        @see setGamma
        """

    def getKernelType(self) -> retval:
        r"""
        Type of a %SVM kernel.
        See SVM::KernelTypes. Default value is SVM::RBF.
        """

    def getNu(self) -> retval:
        r"""
        @see setNu
        """

    def getP(self) -> retval:
        r"""
        @see setP
        """

    def getSupportVectors(self) -> retval:
        r"""
        @brief Retrieves all the support vectors

        The method returns all the support vectors as a floating-point matrix, where support vectors are
        stored as matrix rows.
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getType(self) -> retval:
        r"""
        @see setType
        """

    def getUncompressedSupportVectors(self) -> retval:
        r"""
        @brief Retrieves all the uncompressed support vectors of a linear %SVM

        The method returns all the uncompressed support vectors of a linear %SVM that the compressed
        support vector, used for prediction, was derived from. They are returned in a floating-point
        matrix, where the support vectors are stored as matrix rows.
        """

    def setC(self, val) -> None:
        r"""
        @copybrief getC @see getC
        """

    def setClassWeights(self, val) -> None:
        r"""
        @copybrief getClassWeights @see getClassWeights
        """

    def setCoef0(self, val) -> None:
        r"""
        @copybrief getCoef0 @see getCoef0
        """

    def setDegree(self, val) -> None:
        r"""
        @copybrief getDegree @see getDegree
        """

    def setGamma(self, val) -> None:
        r"""
        @copybrief getGamma @see getGamma
        """

    def setKernel(self, kernelType) -> None:
        r"""
        Initialize with one of predefined kernels.
        See SVM::KernelTypes.
        """

    def setNu(self, val) -> None:
        r"""
        @copybrief getNu @see getNu
        """

    def setP(self, val) -> None:
        r"""
        @copybrief getP @see getP
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def setType(self, val) -> None:
        r"""
        @copybrief getType @see getType
        """

    def trainAuto(self, samples, layout, responses, kFold=..., Cgrid=..., gammaGrid=..., pGrid=..., nuGrid=..., coeffGrid=..., degreeGrid=..., balanced=...) -> retval:
        r"""
        @brief Trains an %SVM with optimal parameters

        @param samples training samples
        @param layout See ml::SampleTypes.
        @param responses vector of responses associated with the training samples.
        @param kFold Cross-validation parameter. The training set is divided into kFold subsets. One subset is used to test the model, the others form the train set. So, the %SVM algorithm is
        @param Cgrid grid for C
        @param gammaGrid grid for gamma
        @param pGrid grid for p
        @param nuGrid grid for nu
        @param coeffGrid grid for coeff
        @param degreeGrid grid for degree
        @param balanced If true and the problem is 2-class classification then the method creates more balanced cross-validation subsets that is proportions between classes in subsets are close to such proportion in the whole train dataset.  The method trains the %SVM model automatically by choosing the optimal parameters C, gamma, p, nu, coef0, degree. Parameters are considered optimal when the cross-validation estimate of the test set error is minimal.  This function only makes use of SVM::getDefaultGrid for parameter optimization and thus only offers rudimentary parameter options.  This function works for the classification (SVM::C_SVC or SVM::NU_SVC) as well as for the regression (SVM::EPS_SVR or SVM::NU_SVR). If it is SVM::ONE_CLASS, no optimization is made and the usual %SVM with parameters specified in params is executed.
        """

    def create(self) -> retval:
        r"""
        Creates empty model.
        Use StatModel::train to train the model. Since %SVM has several parameters, you may want to
        find the best parameters for your problem, it can be done with SVM::trainAuto.
        """

    def getDefaultGridPtr(self, param_id) -> retval:
        r"""
        @brief Generates a grid for %SVM parameters.

        @param param_id %SVM parameters IDs that must be one of the SVM::ParamTypes. The grid is generated for the parameter with this ID.  The function generates a grid pointer for the specified parameter of the %SVM algorithm. The grid may be passed to the function SVM::trainAuto.
        """

    def load(self, filepath) -> retval:
        r"""
        @brief Loads and creates a serialized svm from a file
        *
        * Use SVM::save to serialize and store an SVM to disk.
        * Load the SVM from this file again, by calling this function with the path to the file.
        *
        * @param filepath path to serialized svm
        """

class SVMSGD(StatModel):
    def getInitialStepSize(self) -> retval:
        r"""
        @see setInitialStepSize
        """

    def getMarginRegularization(self) -> retval:
        r"""
        @see setMarginRegularization
        """

    def getMarginType(self) -> retval:
        r"""
        @see setMarginType
        """

    def getShift(self) -> retval:
        r"""
        * @return the shift of the trained model (decision function f(x) = weights * x + shift).
        """

    def getStepDecreasingPower(self) -> retval:
        r"""
        @see setStepDecreasingPower
        """

    def getSvmsgdType(self) -> retval:
        r"""
        @see setSvmsgdType
        """

    def getTermCriteria(self) -> retval:
        r"""
        @see setTermCriteria
        """

    def getWeights(self) -> retval:
        r"""
        * @return the weights of the trained model (decision function f(x) = weights * x + shift).
        """

    def setInitialStepSize(self, InitialStepSize) -> None:
        r"""
        @copybrief getInitialStepSize @see getInitialStepSize
        """

    def setMarginRegularization(self, marginRegularization) -> None:
        r"""
        @copybrief getMarginRegularization @see getMarginRegularization
        """

    def setMarginType(self, marginType) -> None:
        r"""
        @copybrief getMarginType @see getMarginType
        """

    def setOptimalParameters(self, svmsgdType=..., marginType=...) -> None:
        r"""
        @brief Function sets optimal parameters values for chosen SVM SGD model.
        * @param svmsgdType is the type of SVMSGD classifier.
        * @param marginType is the type of margin constraint.
        """

    def setStepDecreasingPower(self, stepDecreasingPower) -> None:
        r"""
        @copybrief getStepDecreasingPower @see getStepDecreasingPower
        """

    def setSvmsgdType(self, svmsgdType) -> None:
        r"""
        @copybrief getSvmsgdType @see getSvmsgdType
        """

    def setTermCriteria(self, val) -> None:
        r"""
        @copybrief getTermCriteria @see getTermCriteria
        """

    def create(self) -> retval:
        r"""
        @brief Creates empty model.
        * Use StatModel::train to train the model. Since %SVMSGD has several parameters, you may want to
        * find the best parameters for your problem or use setOptimalParameters() to set some default parameters.
        """

    def load(self, filepath, nodeName=...) -> retval:
        r"""
        @brief Loads and creates a serialized SVMSGD from a file
        *
        * Use SVMSGD::save to serialize and store an SVMSGD to disk.
        * Load the SVMSGD from this file again, by calling this function with the path to the file.
        * Optionally specify the node for the file containing the classifier
        *
        * @param filepath path to serialized SVMSGD
        * @param nodeName name of node containing the classifier
        """

class StatModel(cv2.Algorithm):
    def calcError(self, data, test, resp=...) -> tuple[retval, resp]:
        r"""
        @brief Computes error on the training or test dataset

        @param data the training data
        @param test if true, the error is computed over the test subset of the data, otherwise it's computed over the training subset of the data. Please note that if you loaded a completely different dataset to evaluate already trained classifier, you will probably want not to set the test subset at all with TrainData::setTrainTestSplitRatio and specify test=false, so that the error is computed for the whole new set. Yes, this sounds a bit confusing.
        @param resp the optional output responses.  The method uses StatModel::predict to compute the error. For regression models the error is computed as RMS, for classifiers - as a percent of missclassified samples (0%-100%).
        """

    def empty(self) -> retval:
        r""""""

    def getVarCount(self) -> retval:
        r"""
        @brief Returns the number of variables in training samples
        """

    def isClassifier(self) -> retval:
        r"""
        @brief Returns true if the model is classifier
        """

    def isTrained(self) -> retval:
        r"""
        @brief Returns true if the model is trained
        """

    def predict(self, samples, results=..., flags=...) -> tuple[retval, results]:
        r"""
        @brief Predicts response(s) for the provided sample(s)

        @param samples The input samples, floating-point matrix
        @param results The optional output matrix of results.
        @param flags The optional flags, model-dependent. See cv::ml::StatModel::Flags.
        """

    @overload
    def train(self, trainData, flags=...) -> retval:
        r"""
        @brief Trains the statistical model

        @param trainData training data that can be loaded from file using TrainData::loadFromCSV or created with TrainData::create.
        @param flags optional flags, depending on the model. Some of the models can be updated with the new training samples, not completely overwritten (such as NormalBayesClassifier or ANN_MLP).
        """

    @overload
    def train(self, samples, layout, responses) -> retval:
        r"""
        @brief Trains the statistical model

        @param samples training samples
        @param layout See ml::SampleTypes.
        @param responses vector of responses associated with the training samples.
        """

class TrainData(builtins.object):
    def getCatCount(self, vi) -> retval:
        r""""""

    def getCatMap(self) -> retval:
        r""""""

    def getCatOfs(self) -> retval:
        r""""""

    def getClassLabels(self) -> retval:
        r"""
        @brief Returns the vector of class labels

        The function returns vector of unique labels occurred in the responses.
        """

    def getDefaultSubstValues(self) -> retval:
        r""""""

    def getLayout(self) -> retval:
        r""""""

    def getMissing(self) -> retval:
        r""""""

    def getNAllVars(self) -> retval:
        r""""""

    def getNSamples(self) -> retval:
        r""""""

    def getNTestSamples(self) -> retval:
        r""""""

    def getNTrainSamples(self) -> retval:
        r""""""

    def getNVars(self) -> retval:
        r""""""

    def getNames(self, names) -> None:
        r"""
        @brief Returns vector of symbolic names captured in loadFromCSV()
        """

    def getNormCatResponses(self) -> retval:
        r""""""

    def getResponseType(self) -> retval:
        r""""""

    def getResponses(self) -> retval:
        r""""""

    def getSample(self, varIdx, sidx, buf) -> None:
        r""""""

    def getSampleWeights(self) -> retval:
        r""""""

    def getSamples(self) -> retval:
        r""""""

    def getTestNormCatResponses(self) -> retval:
        r""""""

    def getTestResponses(self) -> retval:
        r""""""

    def getTestSampleIdx(self) -> retval:
        r""""""

    def getTestSampleWeights(self) -> retval:
        r""""""

    def getTestSamples(self) -> retval:
        r"""
        @brief Returns matrix of test samples
        """

    def getTrainNormCatResponses(self) -> retval:
        r"""
        @brief Returns the vector of normalized categorical responses

        The function returns vector of responses. Each response is integer from `0` to `<number of
        classes>-1`. The actual label value can be retrieved then from the class label vector, see
        TrainData::getClassLabels.
        """

    def getTrainResponses(self) -> retval:
        r"""
        @brief Returns the vector of responses

        The function returns ordered or the original categorical responses. Usually it's used in
        regression algorithms.
        """

    def getTrainSampleIdx(self) -> retval:
        r""""""

    def getTrainSampleWeights(self) -> retval:
        r""""""

    def getTrainSamples(self, layout=..., compressSamples=..., compressVars=...) -> retval:
        r"""
        @brief Returns matrix of train samples

        @param layout The requested layout. If it's different from the initial one, the matrix is transposed. See ml::SampleTypes.
        @param compressSamples if true, the function returns only the training samples (specified by sampleIdx)
        @param compressVars if true, the function returns the shorter training samples, containing only the active variables.  In current implementation the function tries to avoid physical data copying and returns the matrix stored inside TrainData (unless the transposition or compression is needed).
        """

    def getValues(self, vi, sidx, values) -> None:
        r""""""

    def getVarIdx(self) -> retval:
        r""""""

    def getVarSymbolFlags(self) -> retval:
        r""""""

    def getVarType(self) -> retval:
        r""""""

    def setTrainTestSplit(self, count, shuffle=...) -> None:
        r"""
        @brief Splits the training data into the training and test parts
        @sa TrainData::setTrainTestSplitRatio
        """

    def setTrainTestSplitRatio(self, ratio, shuffle=...) -> None:
        r"""
        @brief Splits the training data into the training and test parts

        The function selects a subset of specified relative size and then returns it as the training
        set. If the function is not called, all the data is used for training. Please, note that for
        each of TrainData::getTrain\* there is corresponding TrainData::getTest\*, so that the test
        subset can be retrieved and processed as well.
        @sa TrainData::setTrainTestSplit
        """

    def shuffleTrainTest(self) -> None:
        r""""""

    def create(self, samples, layout, responses, varIdx=..., sampleIdx=..., sampleWeights=..., varType=...) -> retval:
        r"""
        @brief Creates training data from in-memory arrays.

        @param samples matrix of samples. It should have CV_32F type.
        @param layout see ml::SampleTypes.
        @param responses matrix of responses. If the responses are scalar, they should be stored as a single row or as a single column. The matrix should have type CV_32F or CV_32S (in the former case the responses are considered as ordered by default; in the latter case - as categorical)
        @param varIdx vector specifying which variables to use for training. It can be an integer vector (CV_32S) containing 0-based variable indices or byte vector (CV_8U) containing a mask of active variables.
        @param sampleIdx vector specifying which samples to use for training. It can be an integer vector (CV_32S) containing 0-based sample indices or byte vector (CV_8U) containing a mask of training samples.
        @param sampleWeights optional vector with weights for each sample. It should have CV_32F type.
        @param varType optional vector of type CV_8U and size `<number_of_variables_in_samples> + <number_of_variables_in_responses>`, containing types of each input and output variable. See ml::VariableTypes.
        """

    def getSubMatrix(self, matrix, idx, layout) -> retval:
        r"""
        @brief Extract from matrix rows/cols specified by passed indexes.
        @param matrix input matrix (supported types: CV_32S, CV_32F, CV_64F)
        @param idx 1D index vector
        @param layout specifies to extract rows (cv::ml::ROW_SAMPLES) or to extract columns (cv::ml::COL_SAMPLES)
        """

    def getSubVector(self, vec, idx) -> retval:
        r"""
        @brief Extract from 1D vector elements specified by passed indexes.
        @param vec input vector (supported types: CV_32S, CV_32F, CV_64F)
        @param idx 1D index vector
        """

@overload
def ANN_MLP_create() -> retval:
    r"""
    @brief Creates empty model
    """

@overload
def ANN_MLP_create() -> retval:
    r""" """

@overload
def ANN_MLP_create() -> retval:
    r""" """

def ANN_MLP_load(filepath) -> retval:
    r"""
    @brief Loads and creates a serialized ANN from a file
         *
         * Use ANN::save to serialize and store an ANN to disk.
         * Load the ANN from this file again, by calling this function with the path to the file.
         *
         * @param filepath path to serialized ANN
    """

def Boost_create() -> retval:
    r"""
    Creates the empty model.
    Use StatModel::train to train the model, Algorithm::load\<Boost\>(filename) to load the pre-trained model.
    """

def Boost_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized Boost from a file
         *
         * Use Boost::save to serialize and store an RTree to disk.
         * Load the Boost from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized Boost
         * @param nodeName name of node containing the classifier
    """

@overload
def DTrees_create() -> retval:
    r"""
    @brief Creates the empty model
    """

@overload
def DTrees_create() -> retval:
    r""" """

@overload
def DTrees_create() -> retval:
    r""" """

@overload
def DTrees_create() -> retval:
    r""" """

def DTrees_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized DTrees from a file
         *
         * Use DTree::save to serialize and store an DTree to disk.
         * Load the DTree from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized DTree
         * @param nodeName name of node containing the classifier
    """

@overload
def EM_create() -> retval:
    r"""
    Creates empty %EM model.
    """

@overload
def EM_create() -> retval:
    r""" """

@overload
def EM_create() -> retval:
    r""" """

def EM_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized EM from a file
         *
         * Use EM::save to serialize and store an EM to disk.
         * Load the EM from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized EM
         * @param nodeName name of node containing the classifier
    """

@overload
def KNearest_create() -> retval:
    r"""
    @brief Creates the empty model
    """

@overload
def KNearest_create() -> retval:
    r""" """

def KNearest_load(filepath) -> retval:
    r"""
    @brief Loads and creates a serialized knearest from a file
         *
         * Use KNearest::save to serialize and store an KNearest to disk.
         * Load the KNearest from this file again, by calling this function with the path to the file.
         *
         * @param filepath path to serialized KNearest
    """

@overload
def LogisticRegression_create() -> retval:
    r"""
    @brief Creates empty model.
    """

@overload
def LogisticRegression_create() -> retval:
    r""" """

def LogisticRegression_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized LogisticRegression from a file
         *
         * Use LogisticRegression::save to serialize and store an LogisticRegression to disk.
         * Load the LogisticRegression from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized LogisticRegression
         * @param nodeName name of node containing the classifier
    """

def NormalBayesClassifier_create() -> retval:
    r"""
    Creates empty model
    Use StatModel::train to train the model after creation.
    """

def NormalBayesClassifier_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized NormalBayesClassifier from a file
         *
         * Use NormalBayesClassifier::save to serialize and store an NormalBayesClassifier to disk.
         * Load the NormalBayesClassifier from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized NormalBayesClassifier
         * @param nodeName name of node containing the classifier
    """

def ParamGrid_create(minVal=..., maxVal=..., logstep=...) -> retval:
    r"""
    @brief Creates a ParamGrid Ptr that can be given to the %SVM::trainAuto method

        @param minVal minimum value of the parameter grid
        @param maxVal maximum value of the parameter grid
        @param logstep Logarithmic step for iterating the statmodel parameter
    """

@overload
def RTrees_create() -> retval:
    r"""
    Creates the empty model.
    """

@overload
def RTrees_create() -> retval:
    r""" """

@overload
def RTrees_create() -> retval:
    r""" """

def RTrees_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized RTree from a file
         *
         * Use RTree::save to serialize and store an RTree to disk.
         * Load the RTree from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized RTree
         * @param nodeName name of node containing the classifier
    """

def SVMSGD_create() -> retval:
    r"""
    @brief Creates empty model.
         * Use StatModel::train to train the model. Since %SVMSGD has several parameters, you may want to
         * find the best parameters for your problem or use setOptimalParameters() to set some default parameters.
    """

def SVMSGD_load(filepath, nodeName=...) -> retval:
    r"""
    @brief Loads and creates a serialized SVMSGD from a file
         *
         * Use SVMSGD::save to serialize and store an SVMSGD to disk.
         * Load the SVMSGD from this file again, by calling this function with the path to the file.
         * Optionally specify the node for the file containing the classifier
         *
         * @param filepath path to serialized SVMSGD
         * @param nodeName name of node containing the classifier
    """

@overload
def SVM_create() -> retval:
    r"""
    Creates empty model.
    """

@overload
def SVM_create() -> retval:
    r"""
    find the best parameters for your problem, it can be done with SVM::trainAuto.
    """

@overload
def SVM_getDefaultGridPtr(param_id) -> retval:
    r"""
    @brief Generates a grid for %SVM parameters.

        @param param_id %SVM parameters IDs that must be one of the SVM::ParamTypes. The grid is
    """

@overload
def SVM_getDefaultGridPtr(param_id) -> retval:
    r""" """

@overload
def SVM_getDefaultGridPtr(param_id) -> retval:
    r""" """

@overload
def SVM_getDefaultGridPtr(param_id) -> retval:
    r""" """

def SVM_load(filepath) -> retval:
    r"""
    @brief Loads and creates a serialized svm from a file
         *
         * Use SVM::save to serialize and store an SVM to disk.
         * Load the SVM from this file again, by calling this function with the path to the file.
         *
         * @param filepath path to serialized svm
    """

def TrainData_create(samples, layout, responses, varIdx=..., sampleIdx=..., sampleWeights=..., varType=...) -> retval:
    r"""
    @brief Creates training data from in-memory arrays.

        @param samples matrix of samples. It should have CV_32F type.
        @param layout see ml::SampleTypes.
        @param responses matrix of responses. If the responses are scalar, they should be stored as a
            single row or as a single column. The matrix should have type CV_32F or CV_32S (in the
            former case the responses are considered as ordered by default; in the latter case - as
            categorical)
        @param varIdx vector specifying which variables to use for training. It can be an integer vector
            (CV_32S) containing 0-based variable indices or byte vector (CV_8U) containing a mask of
            active variables.
        @param sampleIdx vector specifying which samples to use for training. It can be an integer
            vector (CV_32S) containing 0-based sample indices or byte vector (CV_8U) containing a mask
            of training samples.
        @param sampleWeights optional vector with weights for each sample. It should have CV_32F type.
        @param varType optional vector of type CV_8U and size `<number_of_variables_in_samples> +
            <number_of_variables_in_responses>`, containing types of each input and output variable. See
            ml::VariableTypes.
    """

def TrainData_getSubMatrix(matrix, idx, layout) -> retval:
    r"""
    @brief Extract from matrix rows/cols specified by passed indexes.
        @param matrix input matrix (supported types: CV_32S, CV_32F, CV_64F)
        @param idx 1D index vector
        @param layout specifies to extract rows (cv::ml::ROW_SAMPLES) or to extract columns (cv::ml::COL_SAMPLES)
    """

def TrainData_getSubVector(vec, idx) -> retval:
    r"""
    @brief Extract from 1D vector elements specified by passed indexes.
        @param vec input vector (supported types: CV_32S, CV_32F, CV_64F)
        @param idx 1D index vector
    """

ANN_MLP_ANNEAL: Final[int]
ANN_MLP_BACKPROP: Final[int]
ANN_MLP_GAUSSIAN: Final[int]
ANN_MLP_IDENTITY: Final[int]
ANN_MLP_LEAKYRELU: Final[int]
ANN_MLP_NO_INPUT_SCALE: Final[int]
ANN_MLP_NO_OUTPUT_SCALE: Final[int]
ANN_MLP_RELU: Final[int]
ANN_MLP_RPROP: Final[int]
ANN_MLP_SIGMOID_SYM: Final[int]
ANN_MLP_UPDATE_WEIGHTS: Final[int]
BOOST_DISCRETE: Final[int]
BOOST_GENTLE: Final[int]
BOOST_LOGIT: Final[int]
BOOST_REAL: Final[int]
Boost_DISCRETE: Final[int]
Boost_GENTLE: Final[int]
Boost_LOGIT: Final[int]
Boost_REAL: Final[int]
COL_SAMPLE: Final[int]
DTREES_PREDICT_AUTO: Final[int]
DTREES_PREDICT_MASK: Final[int]
DTREES_PREDICT_MAX_VOTE: Final[int]
DTREES_PREDICT_SUM: Final[int]
DTrees_PREDICT_AUTO: Final[int]
DTrees_PREDICT_MASK: Final[int]
DTrees_PREDICT_MAX_VOTE: Final[int]
DTrees_PREDICT_SUM: Final[int]
EM_COV_MAT_DEFAULT: Final[int]
EM_COV_MAT_DIAGONAL: Final[int]
EM_COV_MAT_GENERIC: Final[int]
EM_COV_MAT_SPHERICAL: Final[int]
EM_DEFAULT_MAX_ITERS: Final[int]
EM_DEFAULT_NCLUSTERS: Final[int]
EM_START_AUTO_STEP: Final[int]
EM_START_E_STEP: Final[int]
EM_START_M_STEP: Final[int]
KNEAREST_BRUTE_FORCE: Final[int]
KNEAREST_KDTREE: Final[int]
KNearest_BRUTE_FORCE: Final[int]
KNearest_KDTREE: Final[int]
LOGISTIC_REGRESSION_BATCH: Final[int]
LOGISTIC_REGRESSION_MINI_BATCH: Final[int]
LOGISTIC_REGRESSION_REG_DISABLE: Final[int]
LOGISTIC_REGRESSION_REG_L1: Final[int]
LOGISTIC_REGRESSION_REG_L2: Final[int]
LogisticRegression_BATCH: Final[int]
LogisticRegression_MINI_BATCH: Final[int]
LogisticRegression_REG_DISABLE: Final[int]
LogisticRegression_REG_L1: Final[int]
LogisticRegression_REG_L2: Final[int]
ROW_SAMPLE: Final[int]
STAT_MODEL_COMPRESSED_INPUT: Final[int]
STAT_MODEL_PREPROCESSED_INPUT: Final[int]
STAT_MODEL_RAW_OUTPUT: Final[int]
STAT_MODEL_UPDATE_MODEL: Final[int]
SVMSGD_ASGD: Final[int]
SVMSGD_HARD_MARGIN: Final[int]
SVMSGD_SGD: Final[int]
SVMSGD_SOFT_MARGIN: Final[int]
SVM_C: Final[int]
SVM_CHI2: Final[int]
SVM_COEF: Final[int]
SVM_CUSTOM: Final[int]
SVM_C_SVC: Final[int]
SVM_DEGREE: Final[int]
SVM_EPS_SVR: Final[int]
SVM_GAMMA: Final[int]
SVM_INTER: Final[int]
SVM_LINEAR: Final[int]
SVM_NU: Final[int]
SVM_NU_SVC: Final[int]
SVM_NU_SVR: Final[int]
SVM_ONE_CLASS: Final[int]
SVM_P: Final[int]
SVM_POLY: Final[int]
SVM_RBF: Final[int]
SVM_SIGMOID: Final[int]
StatModel_COMPRESSED_INPUT: Final[int]
StatModel_PREPROCESSED_INPUT: Final[int]
StatModel_RAW_OUTPUT: Final[int]
StatModel_UPDATE_MODEL: Final[int]
TEST_ERROR: Final[int]
TRAIN_ERROR: Final[int]
VAR_CATEGORICAL: Final[int]
VAR_NUMERICAL: Final[int]
VAR_ORDERED: Final[int]
