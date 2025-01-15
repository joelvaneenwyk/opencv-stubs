import builtins
from typing import Any, Final, overload, TypeAlias

keypoints: TypeAlias = Any
descriptors: TypeAlias = Any
arr: TypeAlias = Any
dst: TypeAlias = Any
retval: TypeAlias = Any

class BufferPool(builtins.object):
    def getAllocator(self) -> retval:
        r""""""

    @overload
    def getBuffer(self, rows, cols, type) -> retval:
        r""""""

    @overload
    def getBuffer(self, size, type) -> retval:
        r""""""

class DeviceInfo(builtins.object):
    def ECCEnabled(self) -> retval:
        r"""

        See help(type(self)) for accurate signature.

        """

    def asyncEngineCount(self) -> retval:
        r""""""

    def canMapHostMemory(self) -> retval:
        r""""""

    def clockRate(self) -> retval:
        r""""""

    def computeMode(self) -> retval:
        r""""""

    def concurrentKernels(self) -> retval:
        r""""""

    def deviceID(self) -> retval:
        r"""
        @brief Returns system index of the CUDA device starting with 0.
        """

    def freeMemory(self) -> retval:
        r""""""

    def integrated(self) -> retval:
        r""""""

    def isCompatible(self) -> retval:
        r"""
        @brief Checks the CUDA module and device compatibility.

        This function returns true if the CUDA module can be run on the specified device. Otherwise, it
        returns false .
        """

    def kernelExecTimeoutEnabled(self) -> retval:
        r""""""

    def l2CacheSize(self) -> retval:
        r""""""

    def majorVersion(self) -> retval:
        r""""""

    def maxGridSize(self) -> retval:
        r""""""

    def maxSurface1D(self) -> retval:
        r""""""

    def maxSurface1DLayered(self) -> retval:
        r""""""

    def maxSurface2D(self) -> retval:
        r""""""

    def maxSurface2DLayered(self) -> retval:
        r""""""

    def maxSurface3D(self) -> retval:
        r""""""

    def maxSurfaceCubemap(self) -> retval:
        r""""""

    def maxSurfaceCubemapLayered(self) -> retval:
        r""""""

    def maxTexture1D(self) -> retval:
        r""""""

    def maxTexture1DLayered(self) -> retval:
        r""""""

    def maxTexture1DLinear(self) -> retval:
        r""""""

    def maxTexture1DMipmap(self) -> retval:
        r""""""

    def maxTexture2D(self) -> retval:
        r""""""

    def maxTexture2DGather(self) -> retval:
        r""""""

    def maxTexture2DLayered(self) -> retval:
        r""""""

    def maxTexture2DLinear(self) -> retval:
        r""""""

    def maxTexture2DMipmap(self) -> retval:
        r""""""

    def maxTexture3D(self) -> retval:
        r""""""

    def maxTextureCubemap(self) -> retval:
        r""""""

    def maxTextureCubemapLayered(self) -> retval:
        r""""""

    def maxThreadsDim(self) -> retval:
        r""""""

    def maxThreadsPerBlock(self) -> retval:
        r""""""

    def maxThreadsPerMultiProcessor(self) -> retval:
        r""""""

    def memPitch(self) -> retval:
        r""""""

    def memoryBusWidth(self) -> retval:
        r""""""

    def memoryClockRate(self) -> retval:
        r""""""

    def minorVersion(self) -> retval:
        r""""""

    def multiProcessorCount(self) -> retval:
        r""""""

    def pciBusID(self) -> retval:
        r""""""

    def pciDeviceID(self) -> retval:
        r""""""

    def pciDomainID(self) -> retval:
        r""""""

    def queryMemory(self, totalMemory, freeMemory) -> None:
        r""""""

    def regsPerBlock(self) -> retval:
        r""""""

    def sharedMemPerBlock(self) -> retval:
        r""""""

    def surfaceAlignment(self) -> retval:
        r""""""

    def tccDriver(self) -> retval:
        r""""""

    def textureAlignment(self) -> retval:
        r""""""

    def texturePitchAlignment(self) -> retval:
        r""""""

    def totalConstMem(self) -> retval:
        r""""""

    def totalGlobalMem(self) -> retval:
        r""""""

    def totalMemory(self) -> retval:
        r""""""

    def unifiedAddressing(self) -> retval:
        r""""""

    def warpSize(self) -> retval:
        r""""""

class Event(builtins.object):
    def queryIfComplete(self) -> retval:
        r""""""

    def record(self, stream=...) -> None:
        r""""""

    def waitForCompletion(self) -> None:
        r""""""

    def elapsedTime(self, start, end) -> retval:
        r""""""

class GpuData(builtins.object): ...

class GpuMat(builtins.object):
    step: int = 0

    class Allocator(builtins.object): ...

    def adjustROI(self, dtop, dbottom, dleft, dright) -> retval:
        r""""""

    def assignTo(self, m, type=...) -> None:
        r""""""

    def channels(self) -> retval:
        r""""""

    def clone(self) -> retval:
        r""""""

    def col(self, x) -> retval:
        r""""""

    @overload
    def colRange(self, startcol, endcol) -> retval:
        r""""""

    @overload
    def colRange(self, r) -> retval:
        r""""""

    @overload
    def convertTo(self, rtype, dst=...) -> dst:
        r""""""

    @overload
    def convertTo(self, rtype, stream, dst=...) -> dst:
        r""""""

    @overload
    def convertTo(self, rtype, alpha, dst=..., beta=...) -> dst:
        r""""""

    @overload
    def convertTo(self, rtype, alpha, stream, dst=...) -> dst:
        r""""""

    def convertTo(self, rtype, alpha, beta, stream, dst=...) -> dst:
        r""""""

    @overload
    def copyTo(self, dst=...) -> dst:
        r""""""

    @overload
    def copyTo(self, stream, dst=...) -> dst:
        r""""""

    @overload
    def copyTo(self, mask, dst=...) -> dst:
        r""""""

    def copyTo(self, mask, stream, dst=...) -> dst:
        r""""""

    @overload
    def create(self, rows, cols, type) -> None:
        r""""""

    @overload
    def create(self, size, type) -> None:
        r""""""

    def cudaPtr(self) -> retval:
        r""""""

    def depth(self) -> retval:
        r""""""

    @overload
    def download(self, dst=...) -> dst:
        r"""
        @brief Performs data download from GpuMat (Blocking call)

        This function copies data from device memory to host memory. As being a blocking call, it is
        guaranteed that the copy operation is finished when this function returns.
        """

    @overload
    def download(self, stream, dst=...) -> dst:
        r"""
        @brief Performs data download from GpuMat (Non-Blocking call)

        This function copies data from device memory to host memory. As being a non-blocking call, this
        function may return even if the copy operation is not finished.

        The copy operation may be overlapped with operations in other non-default streams if \p stream is
        not the default stream and \p dst is HostMem allocated with HostMem::PAGE_LOCKED option.
        """

    def elemSize(self) -> retval:
        r""""""

    def elemSize1(self) -> retval:
        r""""""

    def empty(self) -> retval:
        r""""""

    def isContinuous(self) -> retval:
        r""""""

    def locateROI(self, wholeSize, ofs) -> None:
        r""""""

    def release(self) -> None:
        r""""""

    def reshape(self, cn, rows=...) -> retval:
        r""""""

    def row(self, y) -> retval:
        r""""""

    @overload
    def rowRange(self, startrow, endrow) -> retval:
        r""""""

    @overload
    def rowRange(self, r) -> retval:
        r""""""

    @overload
    def setTo(self, s) -> retval:
        r""""""

    @overload
    def setTo(self, s, stream) -> retval:
        r""""""

    @overload
    def setTo(self, s, mask) -> retval:
        r""""""

    def setTo(self, s, mask, stream) -> retval:
        r""""""

    def size(self) -> retval:
        r""""""

    def step1(self) -> retval:
        r""""""

    def swap(self, mat) -> None:
        r""""""

    def type(self) -> retval:
        r""""""

    def updateContinuityFlag(self) -> None:
        r""""""

    @overload
    def upload(self, arr) -> None:
        r"""
        @brief Performs data upload to GpuMat (Blocking call)

        This function copies data from host memory to device memory. As being a blocking call, it is
        guaranteed that the copy operation is finished when this function returns.
        """

    @overload
    def upload(self, arr, stream) -> None:
        r"""
        @brief Performs data upload to GpuMat (Non-Blocking call)

        This function copies data from host memory to device memory. As being a non-blocking call, this
        function may return even if the copy operation is not finished.

        The copy operation may be overlapped with operations in other non-default streams if \p stream is
        not the default stream and \p dst is HostMem allocated with HostMem::PAGE_LOCKED option.
        """

    def defaultAllocator(self) -> Allocator:
        r""""""

    def setDefaultAllocator(self, allocator) -> None:
        r""""""

class GpuMatND(builtins.object): ...

class HostMem(builtins.object):
    def channels(self) -> retval:
        r""""""

    def clone(self) -> retval:
        r""""""

    def create(self, rows, cols, type) -> None:
        r""""""

    def createMatHeader(self) -> retval:
        r""""""

    def depth(self) -> retval:
        r""""""

    def elemSize(self) -> retval:
        r""""""

    def elemSize1(self) -> retval:
        r""""""

    def empty(self) -> retval:
        r""""""

    def isContinuous(self) -> retval:
        r"""
        @brief Maps CPU memory to GPU address space and creates the cuda::GpuMat header without reference counting
        for it.

        This can be done only if memory was allocated with the SHARED flag and if it is supported by the
        hardware. Laptops often share video and CPU memory, so address spaces can be mapped, which
        eliminates an extra copy.
        """

    def reshape(self, cn, rows=...) -> retval:
        r""""""

    def size(self) -> retval:
        r""""""

    def step1(self) -> retval:
        r""""""

    def swap(self, b) -> None:
        r""""""

    def type(self) -> retval:
        r""""""

class SURF_CUDA(builtins.object):
    def defaultNorm(self) -> retval:
        r""""""

    def descriptorSize(self) -> retval:
        r""""""

    def detect(self, img, mask, keypoints=...) -> keypoints:
        r"""
        @brief Finds the keypoints using fast hessian detector used in SURF

        @param img Source image, currently supports only CV_8UC1 images.
        @param mask A mask image same size as src and of type CV_8UC1.
        @param keypoints Detected keypoints.
        """

    def detectWithDescriptors(self, img, mask, keypoints=..., descriptors=..., useProvidedKeypoints=...) -> tuple[keypoints, descriptors]:
        r"""
        @brief Finds the keypoints and computes their descriptors using fast hessian detector used in SURF

        @param img Source image, currently supports only CV_8UC1 images.
        @param mask A mask image same size as src and of type CV_8UC1.
        @param keypoints Detected keypoints.
        @param descriptors Keypoint descriptors.
        @param useProvidedKeypoints Compute descriptors for the user-provided keypoints and recompute keypoints direction.
        """

    def downloadKeypoints(self, keypointsGPU) -> keypoints:
        r""""""

    def create(self, _hessianThreshold, _nOctaves=..., _nOctaveLayers=..., _extended=..., _keypointsRatio=..., _upright=...) -> retval:
        r"""
        @param _hessianThreshold Threshold for hessian keypoint detector used in SURF.
        @param _nOctaves Number of pyramid octaves the keypoint detector will use.
        @param _nOctaveLayers Number of octave layers within each octave.
        @param _extended Extended descriptor flag (true - use extended 128-element descriptors; false - use 64-element descriptors).
        @param _keypointsRatio
        @param _upright Up-right or rotated features flag (true - do not compute orientation of features; false - compute orientation).
        """

class Stream(builtins.object):
    def cudaPtr(self) -> retval:
        r""""""

    def queryIfComplete(self) -> retval:
        r"""
        @brief Returns true if the current stream queue is finished. Otherwise, it returns false.
        """

    def waitEvent(self, event) -> None:
        r"""
        @brief Makes a compute stream wait on an event.
        """

    def waitForCompletion(self) -> None:
        r"""
        @brief Blocks the current CPU thread until all operations in the stream are complete.
        """

    def Null(self) -> retval:
        r"""
        @brief Adds a callback to be called on the host after all currently enqueued items in the stream have
        completed.

        @note Callbacks must not make any CUDA API calls. Callbacks must not perform any synchronization
        that may depend on outstanding device work or other callbacks that are not mandated to run earlier.
        Callbacks without a mandated order (in independent streams) execute in undefined order and may be
        serialized.
        type
        See help(type) for accurate signature.
        """

class TargetArchs(builtins.object):
    def has(self, major, minor) -> retval:
        r"""
        @brief There is a set of methods to check whether the module contains intermediate (PTX) or binary CUDA
        code for the given architecture(s):

        @param major Major compute capability version.
        @param minor Minor compute capability version.
        """

    def hasBin(self, major, minor) -> retval:
        r""""""

    def hasEqualOrGreater(self, major, minor) -> retval:
        r""""""

    def hasEqualOrGreaterBin(self, major, minor) -> retval:
        r""""""

    def hasEqualOrGreaterPtx(self, major, minor) -> retval:
        r""""""

    def hasEqualOrLessPtx(self, major, minor) -> retval:
        r""""""

    def hasPtx(self, major, minor) -> retval:
        r""""""

def Event_elapsedTime(start, end) -> retval:
    """
    .
    """

def GpuMat_defaultAllocator() -> retval:
    """
    .
    """

def GpuMat_setDefaultAllocator(allocator) -> None:
    """
    .
    """

@overload
def SURF_CUDA_create(_hessianThreshold, _nOctaves=..., _nOctaveLayers=..., _extended=..., _keypointsRatio=..., _upright=...) -> retval:
    """
    @param _hessianThreshold Threshold for hessian keypoint detector used in SURF.
        @param _nOctaves Number of pyramid octaves the keypoint detector will use.
        @param _nOctaveLayers Number of octave layers within each octave.
        @param _extended Extended descriptor flag (true - use extended 128-element descriptors; false - use
        64-element descriptors).
        @param _keypointsRatio
        @param _upright Up-right or rotated features flag (true - do not compute orientation of features;
    """

@overload
def SURF_CUDA_create(_hessianThreshold, _nOctaves=..., _nOctaveLayers=..., _extended=..., _keypointsRatio=..., _upright=...) -> retval:
    """ """

@overload
def Stream_Null() -> retval:
    """
    @brief Adds a callback to be called on the host after all currently enqueued items in the stream have
    """

@overload
def Stream_Null() -> retval:
    """

    @note Callbacks must not make any CUDA API calls. Callbacks must not perform any synchronization
    """

@overload
def Stream_Null() -> retval:
    """ """

@overload
def Stream_Null() -> retval:
    """ """

@overload
def Stream_Null() -> retval:
    """ """

@overload
def TargetArchs_has(major, minor) -> retval:
    """
    @brief There is a set of methods to check whether the module contains intermediate (PTX) or binary CUDA
    """

@overload
def TargetArchs_has(major, minor) -> retval:
    """

    @param major Major compute capability version.
    @param minor Minor compute capability version.
    """

def TargetArchs_hasBin(major, minor) -> retval:
    """
    .
    """

def TargetArchs_hasEqualOrGreater(major, minor) -> retval:
    """
    .
    """

def TargetArchs_hasEqualOrGreaterBin(major, minor) -> retval:
    """
    .
    """

def TargetArchs_hasEqualOrGreaterPtx(major, minor) -> retval:
    """
    .
    """

def TargetArchs_hasEqualOrLessPtx(major, minor) -> retval:
    """
    .
    """

def TargetArchs_hasPtx(major, minor) -> retval:
    """
    .
    """

def createContinuous(rows, cols, type, arr=...) -> arr:
    """
    @brief Creates a continuous matrix.

    @param rows Row count.
    @param cols Column count.
    @param type Type of the matrix.
    @param arr Destination matrix. This parameter changes only if it has a proper type and area (
    \f$\texttt{rows} \times \texttt{cols}\f$ ).

    Matrix is called continuous if its elements are stored continuously, that is, without gaps at the
    end of each row.
    """

def ensureSizeIsEnough(rows, cols, type, arr=...) -> arr:
    """
    @brief Ensures that the size of a matrix is big enough and the matrix has a proper type.

    @param rows Minimum desired number of rows.
    @param cols Minimum desired number of columns.
    @param type Desired matrix type.
    @param arr Destination matrix.

    The function does not reallocate memory if the matrix has proper attributes already.
    """

def fastNlMeansDenoising(src, h, dst=..., search_window=..., block_size=..., stream=...) -> dst:
    """
    @brief Perform image denoising using Non-local Means Denoising algorithm
    <http://www.ipol.im/pub/algo/bcm_non_local_means_denoising> with several computational
    optimizations. Noise expected to be a gaussian white noise

    @param src Input 8-bit 1-channel, 2-channel or 3-channel image.
    @param dst Output image with the same size and type as src .
    @param h Parameter regulating filter strength. Big h value perfectly removes noise but also
    removes image details, smaller h value preserves details but also preserves some noise
    @param search_window Size in pixels of the window that is used to compute weighted average for
    given pixel. Should be odd. Affect performance linearly: greater search_window - greater
    denoising time. Recommended value 21 pixels
    @param block_size Size in pixels of the template patch that is used to compute weights. Should be
    odd. Recommended value 7 pixels
    @param stream Stream for the asynchronous invocations.

    This function expected to be applied to grayscale images. For colored images look at
    FastNonLocalMeansDenoising::labMethod.

    @sa
       fastNlMeansDenoising
    """

def fastNlMeansDenoisingColored(src, h_luminance, photo_render, dst=..., search_window=..., block_size=..., stream=...) -> dst:
    """
    @brief Modification of fastNlMeansDenoising function for colored images

    @param src Input 8-bit 3-channel image.
    @param dst Output image with the same size and type as src .
    @param h_luminance Parameter regulating filter strength. Big h value perfectly removes noise but
    also removes image details, smaller h value preserves details but also preserves some noise
    @param photo_render float The same as h but for color components. For most images value equals 10 will be
    enough to remove colored noise and do not distort colors
    @param search_window Size in pixels of the window that is used to compute weighted average for
    given pixel. Should be odd. Affect performance linearly: greater search_window - greater
    denoising time. Recommended value 21 pixels
    @param block_size Size in pixels of the template patch that is used to compute weights. Should be
    odd. Recommended value 7 pixels
    @param stream Stream for the asynchronous invocations.

    The function converts image to CIELAB colorspace and then separately denoise L and AB components
    with given h parameters using FastNonLocalMeansDenoising::simpleMethod function.

    @sa
       fastNlMeansDenoisingColored
    """

def getCudaEnabledDeviceCount() -> retval:
    """
    @brief Returns the number of installed CUDA-enabled devices.

    Use this function before any other CUDA functions calls. If OpenCV is compiled without CUDA support,
    this function returns 0. If the CUDA driver is not installed, or is incompatible, this function
    returns -1.
    """

def getDevice() -> retval:
    """
    @brief Returns the current device index set by cuda::setDevice or initialized by default.
    """

def nonLocalMeans(src, h, dst=..., search_window=..., block_size=..., borderMode=..., stream=...) -> dst:
    """
    @brief Performs pure non local means denoising without any simplification, and thus it is not fast.

    @param src Source image. Supports only CV_8UC1, CV_8UC2 and CV_8UC3.
    @param dst Destination image.
    @param h Filter sigma regulating filter strength for color.
    @param search_window Size of search window.
    @param block_size Size of block used for computing weights.
    @param borderMode Border type. See borderInterpolate for details. BORDER_REFLECT101 ,
    BORDER_REPLICATE , BORDER_CONSTANT , BORDER_REFLECT and BORDER_WRAP are supported for now.
    @param stream Stream for the asynchronous version.

    @sa
       fastNlMeansDenoising
    """

def printCudaDeviceInfo(device) -> None:
    """
    .
    """

def printShortCudaDeviceInfo(device) -> None:
    """
    .
    """

def registerPageLocked(m) -> None:
    """
    @brief Page-locks the memory of matrix and maps it for the device(s).

    @param m Input matrix.
    """

def resetDevice() -> None:
    """
    @brief Explicitly destroys and cleans up all resources associated with the current device in the current
    process.

    Any subsequent API call to this device will reinitialize the device.
    """

def setBufferPoolConfig(deviceId, stackSize, stackCount) -> None:
    """
    .
    """

def setBufferPoolUsage(on) -> None:
    """
    .
    """

def setDevice(device) -> None:
    """
    @brief Sets a device and initializes it for the current thread.

    @param device System index of a CUDA device starting with 0.

    If the call of this function is omitted, a default device is initialized at the fist CUDA usage.
    """

def unregisterPageLocked(m) -> None:
    """
    @brief Unmaps the memory of matrix and makes it pageable again.

    @param m Input matrix.
    """

DEVICE_INFO_COMPUTE_MODE_DEFAULT: Final[int]
DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE: Final[int]
DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE_PROCESS: Final[int]
DEVICE_INFO_COMPUTE_MODE_PROHIBITED: Final[int]
DYNAMIC_PARALLELISM: Final[int]
DeviceInfo_ComputeModeDefault: Final[int]
DeviceInfo_ComputeModeExclusive: Final[int]
DeviceInfo_ComputeModeExclusiveProcess: Final[int]
DeviceInfo_ComputeModeProhibited: Final[int]
EVENT_BLOCKING_SYNC: Final[int]
EVENT_DEFAULT: Final[int]
EVENT_DISABLE_TIMING: Final[int]
EVENT_INTERPROCESS: Final[int]
Event_BLOCKING_SYNC: Final[int]
Event_DEFAULT: Final[int]
Event_DISABLE_TIMING: Final[int]
Event_INTERPROCESS: Final[int]
FEATURE_SET_COMPUTE_10: int
FEATURE_SET_COMPUTE_11: Final[int]
FEATURE_SET_COMPUTE_12: Final[int]
FEATURE_SET_COMPUTE_13: Final[int]
FEATURE_SET_COMPUTE_20: int
FEATURE_SET_COMPUTE_21: Final[int]
FEATURE_SET_COMPUTE_30: int
FEATURE_SET_COMPUTE_32: Final[int]
FEATURE_SET_COMPUTE_35: Final[int]
FEATURE_SET_COMPUTE_50: int
GLOBAL_ATOMICS: Final[int]
HOST_MEM_PAGE_LOCKED: Final[int]
HOST_MEM_SHARED: Final[int]
HOST_MEM_WRITE_COMBINED: Final[int]
HostMem_PAGE_LOCKED: Final[int]
HostMem_SHARED: Final[int]
HostMem_WRITE_COMBINED: Final[int]
NATIVE_DOUBLE: Final[int]
SHARED_ATOMICS: Final[int]
SURF_CUDA_ANGLE_ROW: Final[int]
SURF_CUDA_HESSIAN_ROW: Final[int]
SURF_CUDA_LAPLACIAN_ROW: Final[int]
SURF_CUDA_OCTAVE_ROW: Final[int]
SURF_CUDA_ROWS_COUNT: Final[int]
SURF_CUDA_SIZE_ROW: Final[int]
SURF_CUDA_X_ROW: Final[int]
SURF_CUDA_Y_ROW: Final[int]
WARP_SHUFFLE_FUNCTIONS: Final[int]
