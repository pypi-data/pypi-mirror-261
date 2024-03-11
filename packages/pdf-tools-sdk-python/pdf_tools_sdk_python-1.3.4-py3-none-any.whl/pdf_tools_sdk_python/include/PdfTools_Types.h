/******************************************************************************
 *
 * File:            PdfTools_Types.h
 *
 * Description:     Types definition for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_TYPES_H__
#define PDFTOOLS_TYPES_H__

#ifndef BOOL
#define BOOL  int
#define TRUE  1
#define FALSE 0
#endif

#ifdef __cplusplus
extern "C"
{
#endif

typedef enum TPdfTools_ErrorCode
{
    ePdfTools_Error_Success              = 0,
    ePdfTools_Error_UnsupportedOperation = 1,
    ePdfTools_Error_IllegalState         = 2,
    ePdfTools_Error_IllegalArgument      = 3,
    ePdfTools_Error_IO                   = 4,
    ePdfTools_Error_NotFound             = 5,
    ePdfTools_Error_Unknown              = 6,
    ePdfTools_Error_Generic              = 10,
    ePdfTools_Error_License              = 12,
    ePdfTools_Error_UnknownFormat        = 15,
    ePdfTools_Error_Corrupt              = 16,
    ePdfTools_Error_Password             = 17,
    ePdfTools_Error_Conformance          = 18,
    ePdfTools_Error_UnsupportedFeature   = 19,
    ePdfTools_Error_Processing           = 21,
    ePdfTools_Error_Exists               = 22,
    ePdfTools_Error_Permission           = 23,
    ePdfTools_Error_Http                 = 24,
    ePdfTools_Error_Retry                = 25,
} TPdfTools_ErrorCode;

typedef enum TPdfToolsPdf_Permission
{
    ePdfToolsPdf_Permission_None                = 0,
    ePdfToolsPdf_Permission_Print               = 4,
    ePdfToolsPdf_Permission_Modify              = 8,
    ePdfToolsPdf_Permission_Copy                = 16,
    ePdfToolsPdf_Permission_Annotate            = 32,
    ePdfToolsPdf_Permission_FillForms           = 256,
    ePdfToolsPdf_Permission_SupportDisabilities = 512,
    ePdfToolsPdf_Permission_Assemble            = 1024,
    ePdfToolsPdf_Permission_DigitalPrint        = 2048,
    ePdfToolsPdf_Permission_All                 = 3900,
} TPdfToolsPdf_Permission;

typedef enum TPdfToolsPdf_XfaType
{
    ePdfToolsPdf_XfaType_NoXfa             = 0,
    ePdfToolsPdf_XfaType_XfaNeedsRendering = 1,
    ePdfToolsPdf_XfaType_XfaRendered       = 2,
} TPdfToolsPdf_XfaType;

typedef enum TPdfToolsPdf_MdpPermissions
{
    ePdfToolsPdf_MdpPermissions_NoChanges   = 1,
    ePdfToolsPdf_MdpPermissions_FormFilling = 2,
    ePdfToolsPdf_MdpPermissions_Annotate    = 3,
} TPdfToolsPdf_MdpPermissions;

typedef enum TPdfToolsPdf_Conformance
{
    ePdfToolsPdf_Conformance_Pdf10  = 0x1000,
    ePdfToolsPdf_Conformance_Pdf11  = 0x1100,
    ePdfToolsPdf_Conformance_Pdf12  = 0x1200,
    ePdfToolsPdf_Conformance_Pdf13  = 0x1300,
    ePdfToolsPdf_Conformance_Pdf14  = 0x1400,
    ePdfToolsPdf_Conformance_Pdf15  = 0x1500,
    ePdfToolsPdf_Conformance_Pdf16  = 0x1600,
    ePdfToolsPdf_Conformance_Pdf17  = 0x1700,
    ePdfToolsPdf_Conformance_Pdf20  = 0x2000,
    ePdfToolsPdf_Conformance_PdfA1B = 0x1401,
    ePdfToolsPdf_Conformance_PdfA1A = 0x1402,
    ePdfToolsPdf_Conformance_PdfA2B = 0x1701,
    ePdfToolsPdf_Conformance_PdfA2U = 0x1702,
    ePdfToolsPdf_Conformance_PdfA2A = 0x1703,
    ePdfToolsPdf_Conformance_PdfA3B = 0x1711,
    ePdfToolsPdf_Conformance_PdfA3U = 0x1712,
    ePdfToolsPdf_Conformance_PdfA3A = 0x1713,
} TPdfToolsPdf_Conformance;

typedef enum TPdfToolsDocumentAssembly_CopyStrategy
{
    ePdfToolsDocumentAssembly_CopyStrategy_Copy    = 1,
    ePdfToolsDocumentAssembly_CopyStrategy_Flatten = 2,
    ePdfToolsDocumentAssembly_CopyStrategy_Remove  = 3,
} TPdfToolsDocumentAssembly_CopyStrategy;

typedef enum TPdfToolsDocumentAssembly_RemovalStrategy
{
    ePdfToolsDocumentAssembly_RemovalStrategy_Flatten = 1,
    ePdfToolsDocumentAssembly_RemovalStrategy_Remove  = 2,
} TPdfToolsDocumentAssembly_RemovalStrategy;

typedef enum TPdfToolsDocumentAssembly_NamedDestinationCopyStrategy
{
    ePdfToolsDocumentAssembly_NamedDestinationCopyStrategy_Copy    = 1,
    ePdfToolsDocumentAssembly_NamedDestinationCopyStrategy_Resolve = 2,
} TPdfToolsDocumentAssembly_NamedDestinationCopyStrategy;

typedef enum TPdfToolsDocumentAssembly_NameConflictResolution
{
    ePdfToolsDocumentAssembly_NameConflictResolution_Merge  = 1,
    ePdfToolsDocumentAssembly_NameConflictResolution_Rename = 2,
} TPdfToolsDocumentAssembly_NameConflictResolution;

typedef enum TPdfToolsOptimization_ConversionStrategy
{
    ePdfToolsOptimization_ConversionStrategy_Copy    = 1,
    ePdfToolsOptimization_ConversionStrategy_Flatten = 2,
} TPdfToolsOptimization_ConversionStrategy;

typedef enum TPdfToolsOptimization_RemovalStrategy
{
    ePdfToolsOptimization_RemovalStrategy_Flatten = 2,
    ePdfToolsOptimization_RemovalStrategy_Remove  = 3,
} TPdfToolsOptimization_RemovalStrategy;

typedef enum TPdfToolsOptimization_CompressionAlgorithmSelection
{
    ePdfToolsOptimization_CompressionAlgorithmSelection_PreserveQuality = 1,
    ePdfToolsOptimization_CompressionAlgorithmSelection_Balanced        = 2,
    ePdfToolsOptimization_CompressionAlgorithmSelection_Speed           = 3,
} TPdfToolsOptimization_CompressionAlgorithmSelection;

typedef enum TPdfToolsPdf2Image_FaxVerticalResolution
{
    ePdfToolsPdf2Image_FaxVerticalResolution_Standard = 1,
    ePdfToolsPdf2Image_FaxVerticalResolution_High     = 2,
} TPdfToolsPdf2Image_FaxVerticalResolution;

typedef enum TPdfToolsPdf2Image_TiffBitonalCompressionType
{
    ePdfToolsPdf2Image_TiffBitonalCompressionType_G3 = 1,
    ePdfToolsPdf2Image_TiffBitonalCompressionType_G4 = 2,
} TPdfToolsPdf2Image_TiffBitonalCompressionType;

typedef enum TPdfToolsPdf2Image_BackgroundType
{
    ePdfToolsPdf2Image_BackgroundType_White       = 1,
    ePdfToolsPdf2Image_BackgroundType_Transparent = 2,
} TPdfToolsPdf2Image_BackgroundType;

typedef enum TPdfToolsPdf2Image_PngColorSpace
{
    ePdfToolsPdf2Image_PngColorSpace_Rgb  = 1,
    ePdfToolsPdf2Image_PngColorSpace_Gray = 2,
} TPdfToolsPdf2Image_PngColorSpace;

typedef enum TPdfToolsPdf2Image_JpegColorSpace
{
    ePdfToolsPdf2Image_JpegColorSpace_Rgb  = 1,
    ePdfToolsPdf2Image_JpegColorSpace_Gray = 2,
    ePdfToolsPdf2Image_JpegColorSpace_Cmyk = 3,
} TPdfToolsPdf2Image_JpegColorSpace;

typedef enum TPdfToolsPdf2Image_ColorSpace
{
    ePdfToolsPdf2Image_ColorSpace_Rgb  = 1,
    ePdfToolsPdf2Image_ColorSpace_Gray = 2,
    ePdfToolsPdf2Image_ColorSpace_Cmyk = 3,
} TPdfToolsPdf2Image_ColorSpace;

typedef enum TPdfToolsPdf2Image_AnnotationOptions
{
    ePdfToolsPdf2Image_AnnotationOptions_ShowAnnotations          = 1,
    ePdfToolsPdf2Image_AnnotationOptions_ShowAnnotationsAndPopups = 2,
} TPdfToolsPdf2Image_AnnotationOptions;

typedef enum TPdfToolsPdfAValidation_ErrorCategory
{
    ePdfToolsPdfAValidation_ErrorCategory_Format                = 0x00000001,
    ePdfToolsPdfAValidation_ErrorCategory_Pdf                   = 0x00000002,
    ePdfToolsPdfAValidation_ErrorCategory_Encryption            = 0x00000004,
    ePdfToolsPdfAValidation_ErrorCategory_Color                 = 0x00000008,
    ePdfToolsPdfAValidation_ErrorCategory_Rendering             = 0x00000010,
    ePdfToolsPdfAValidation_ErrorCategory_Alternate             = 0x00000020,
    ePdfToolsPdfAValidation_ErrorCategory_PostScript            = 0x00000040,
    ePdfToolsPdfAValidation_ErrorCategory_External              = 0x00000080,
    ePdfToolsPdfAValidation_ErrorCategory_Font                  = 0x00000100,
    ePdfToolsPdfAValidation_ErrorCategory_Unicode               = 0x00000200,
    ePdfToolsPdfAValidation_ErrorCategory_Transparency          = 0x00000400,
    ePdfToolsPdfAValidation_ErrorCategory_UnsupportedAnnotation = 0x00000800,
    ePdfToolsPdfAValidation_ErrorCategory_Multimedia            = 0x00001000,
    ePdfToolsPdfAValidation_ErrorCategory_Print                 = 0x00002000,
    ePdfToolsPdfAValidation_ErrorCategory_Appearance            = 0x00004000,
    ePdfToolsPdfAValidation_ErrorCategory_Action                = 0x00008000,
    ePdfToolsPdfAValidation_ErrorCategory_Metadata              = 0x00010000,
    ePdfToolsPdfAValidation_ErrorCategory_Structure             = 0x00020000,
    ePdfToolsPdfAValidation_ErrorCategory_OptionalContent       = 0x00040000,
    ePdfToolsPdfAValidation_ErrorCategory_EmbeddedFile          = 0x00080000,
    ePdfToolsPdfAValidation_ErrorCategory_Signature             = 0x00100000,
    ePdfToolsPdfAValidation_ErrorCategory_Custom                = 0x40000000,
} TPdfToolsPdfAValidation_ErrorCategory;

typedef enum TPdfToolsPdfAConversion_EventSeverity
{
    ePdfToolsPdfAConversion_EventSeverity_Information = 1,
    ePdfToolsPdfAConversion_EventSeverity_Warning     = 2,
    ePdfToolsPdfAConversion_EventSeverity_Error       = 3,
} TPdfToolsPdfAConversion_EventSeverity;

typedef enum TPdfToolsPdfAConversion_EventCategory
{
    ePdfToolsPdfAConversion_EventCategory_VisualDifferences      = 0x00000001,
    ePdfToolsPdfAConversion_EventCategory_RepairedCorruption     = 0x00000002,
    ePdfToolsPdfAConversion_EventCategory_ManagedColors          = 0x00000004,
    ePdfToolsPdfAConversion_EventCategory_ChangedColorant        = 0x00000008,
    ePdfToolsPdfAConversion_EventCategory_RemovedExternalContent = 0x00000010,
    ePdfToolsPdfAConversion_EventCategory_ConvertedFont          = 0x00000020,
    ePdfToolsPdfAConversion_EventCategory_SubstitutedFont        = 0x00000040,
    ePdfToolsPdfAConversion_EventCategory_RemovedTransparency    = 0x00000080,
    ePdfToolsPdfAConversion_EventCategory_RemovedAnnotation      = 0x00000100,
    ePdfToolsPdfAConversion_EventCategory_RemovedMultimedia      = 0x00000200,
    ePdfToolsPdfAConversion_EventCategory_RemovedAction          = 0x00000400,
    ePdfToolsPdfAConversion_EventCategory_RemovedMetadata        = 0x00000800,
    ePdfToolsPdfAConversion_EventCategory_RemovedStructure       = 0x00001000,
    ePdfToolsPdfAConversion_EventCategory_RemovedOptionalContent = 0x00002000,
    ePdfToolsPdfAConversion_EventCategory_ConvertedEmbeddedFile  = 0x00004000,
    ePdfToolsPdfAConversion_EventCategory_RemovedEmbeddedFile    = 0x00008000,
    ePdfToolsPdfAConversion_EventCategory_RemovedSignature       = 0x00010000,
} TPdfToolsPdfAConversion_EventCategory;

typedef enum TPdfToolsPdfAConversion_EventCode
{
    ePdfToolsPdfAConversion_EventCode_Generic                         = 0x00000001,
    ePdfToolsPdfAConversion_EventCode_RemovedXfa                      = 0x01000000,
    ePdfToolsPdfAConversion_EventCode_FontNonEmbeddedOrderingIdentity = 0x01000001,
    ePdfToolsPdfAConversion_EventCode_FontNoRotate                    = 0x01000002,
    ePdfToolsPdfAConversion_EventCode_FontNoItalicSimulation          = 0x01000003,
    ePdfToolsPdfAConversion_EventCode_ClippedNumberValue              = 0x01000004,
    ePdfToolsPdfAConversion_EventCode_RecoveredImageSize              = 0x02000000,
    ePdfToolsPdfAConversion_EventCode_RepairedFont                    = 0x02000001,
    ePdfToolsPdfAConversion_EventCode_CopiedOutputIntent              = 0x03000000,
    ePdfToolsPdfAConversion_EventCode_SetOutputIntent                 = 0x03000001,
    ePdfToolsPdfAConversion_EventCode_GeneratedOutputIntent           = 0x03000002,
    ePdfToolsPdfAConversion_EventCode_SetColorProfile                 = 0x03000003,
    ePdfToolsPdfAConversion_EventCode_GeneratedColorProfile           = 0x03000004,
    ePdfToolsPdfAConversion_EventCode_CreatedCalibrated               = 0x03000005,
    ePdfToolsPdfAConversion_EventCode_RenamedColorant                 = 0x04000000,
    ePdfToolsPdfAConversion_EventCode_ResolvedColorantCollision       = 0x04000001,
    ePdfToolsPdfAConversion_EventCode_EmbededFont                     = 0x06000000,
    ePdfToolsPdfAConversion_EventCode_SubstitutedFont                 = 0x07000000,
    ePdfToolsPdfAConversion_EventCode_SubstitutedMultipleMaster       = 0x07000001,
    ePdfToolsPdfAConversion_EventCode_ConvertedToStamp                = 0x09000000,
    ePdfToolsPdfAConversion_EventCode_RemovedDocumentMetadata         = 0x0C000000,
    ePdfToolsPdfAConversion_EventCode_CopiedEmbeddedFile              = 0x0F000000,
    ePdfToolsPdfAConversion_EventCode_ConvertingEmbeddedFileStart     = 0x0F000001,
    ePdfToolsPdfAConversion_EventCode_ConvertingEmbeddedFileSuccess   = 0x0F000002,
    ePdfToolsPdfAConversion_EventCode_ChangedToInitialDocument        = 0x10000000,
    ePdfToolsPdfAConversion_EventCode_ConvertingEmbeddedFileError     = 0x10000001,
    ePdfToolsPdfAConversion_EventCode_RemovedEmbeddedFile             = 0x10000002,
    ePdfToolsPdfAConversion_EventCode_RemovedFileAttachmentAnnotation = 0x10000003,
} TPdfToolsPdfAConversion_EventCode;

typedef enum TPdfToolsSign_WarningCategory
{
    ePdfToolsSign_WarningCategory_PdfARemoved                    = 1,
    ePdfToolsSign_WarningCategory_SignedDocEncryptionUnchanged   = 2,
    ePdfToolsSign_WarningCategory_AddValidationInformationFailed = 3,
} TPdfToolsSign_WarningCategory;

typedef enum TPdfToolsSign_SignatureRemoval
{
    ePdfToolsSign_SignatureRemoval_None   = 1,
    ePdfToolsSign_SignatureRemoval_Signed = 2,
    ePdfToolsSign_SignatureRemoval_All    = 3,
} TPdfToolsSign_SignatureRemoval;

typedef enum TPdfToolsSign_AddValidationInformation
{
    ePdfToolsSign_AddValidationInformation_None   = 1,
    ePdfToolsSign_AddValidationInformation_Latest = 2,
    ePdfToolsSign_AddValidationInformation_All    = 3,
} TPdfToolsSign_AddValidationInformation;

typedef enum TPdfToolsCrypto_HashAlgorithm
{
    ePdfToolsCrypto_HashAlgorithm_Md5       = 1,
    ePdfToolsCrypto_HashAlgorithm_RipeMd160 = 2,
    ePdfToolsCrypto_HashAlgorithm_Sha1      = 3,
    ePdfToolsCrypto_HashAlgorithm_Sha256    = 4,
    ePdfToolsCrypto_HashAlgorithm_Sha384    = 5,
    ePdfToolsCrypto_HashAlgorithm_Sha512    = 6,
    ePdfToolsCrypto_HashAlgorithm_Sha3_256  = 7,
    ePdfToolsCrypto_HashAlgorithm_Sha3_384  = 8,
    ePdfToolsCrypto_HashAlgorithm_Sha3_512  = 9,
} TPdfToolsCrypto_HashAlgorithm;

typedef enum TPdfToolsCrypto_SignatureAlgorithm
{
    ePdfToolsCrypto_SignatureAlgorithm_RsaRsa    = 1,
    ePdfToolsCrypto_SignatureAlgorithm_RsaSsaPss = 2,
    ePdfToolsCrypto_SignatureAlgorithm_Ecdsa     = 3,
} TPdfToolsCrypto_SignatureAlgorithm;

typedef enum TPdfToolsCrypto_SignaturePaddingType
{
    ePdfToolsCrypto_SignaturePaddingType_Default   = 0,
    ePdfToolsCrypto_SignaturePaddingType_RsaRsa    = 1,
    ePdfToolsCrypto_SignaturePaddingType_RsaSsaPss = 2,
} TPdfToolsCrypto_SignaturePaddingType;

typedef enum TPdfToolsCrypto_SignatureFormat
{
    ePdfToolsCrypto_SignatureFormat_AdbePkcs7Detached = 1,
    ePdfToolsCrypto_SignatureFormat_EtsiCadesDetached = 2,
} TPdfToolsCrypto_SignatureFormat;

typedef enum TPdfToolsCrypto_ValidationInformation
{
    ePdfToolsCrypto_ValidationInformation_None             = 0,
    ePdfToolsCrypto_ValidationInformation_EmbedInSignature = 1,
    ePdfToolsCrypto_ValidationInformation_EmbedInDocument  = 2,
} TPdfToolsCrypto_ValidationInformation;

typedef enum TPdfToolsSignatureValidation_Indication
{
    ePdfToolsSignatureValidation_Indication_Valid         = 1,
    ePdfToolsSignatureValidation_Indication_Invalid       = 2,
    ePdfToolsSignatureValidation_Indication_Indeterminate = 3,
} TPdfToolsSignatureValidation_Indication;

typedef enum TPdfToolsSignatureValidation_SubIndication
{
    ePdfToolsSignatureValidation_SubIndication_Revoked                            = 1,
    ePdfToolsSignatureValidation_SubIndication_HashFailure                        = 2,
    ePdfToolsSignatureValidation_SubIndication_SigCryptoFailure                   = 3,
    ePdfToolsSignatureValidation_SubIndication_SigConstraintsFailure              = 4,
    ePdfToolsSignatureValidation_SubIndication_ChainConstraintsFailure            = 5,
    ePdfToolsSignatureValidation_SubIndication_CryptoConstraintsFailure           = 6,
    ePdfToolsSignatureValidation_SubIndication_Expired                            = 7,
    ePdfToolsSignatureValidation_SubIndication_NotYetValid                        = 8,
    ePdfToolsSignatureValidation_SubIndication_FormatFailure                      = 9,
    ePdfToolsSignatureValidation_SubIndication_PolicyProcessingError              = 10,
    ePdfToolsSignatureValidation_SubIndication_UnknownCommitmentType              = 11,
    ePdfToolsSignatureValidation_SubIndication_TimestampOrderFailure              = 12,
    ePdfToolsSignatureValidation_SubIndication_NoSignerCertificateFound           = 13,
    ePdfToolsSignatureValidation_SubIndication_NoCertificateChainFound            = 14,
    ePdfToolsSignatureValidation_SubIndication_RevokedNoPoe                       = 15,
    ePdfToolsSignatureValidation_SubIndication_RevokedCaNoPoe                     = 16,
    ePdfToolsSignatureValidation_SubIndication_OutOfBoundsNoPoe                   = 17,
    ePdfToolsSignatureValidation_SubIndication_CryptoConstraintsFailureNoPoe      = 18,
    ePdfToolsSignatureValidation_SubIndication_NoPoe                              = 19,
    ePdfToolsSignatureValidation_SubIndication_TryLater                           = 20,
    ePdfToolsSignatureValidation_SubIndication_NoPolicy                           = 21,
    ePdfToolsSignatureValidation_SubIndication_SignedDataNotFound                 = 22,
    ePdfToolsSignatureValidation_SubIndication_IncompleteCertificateChain         = 512,
    ePdfToolsSignatureValidation_SubIndication_CertificateNoRevocationInformation = 513,
    ePdfToolsSignatureValidation_SubIndication_MissingRevocationInformation       = 514,
    ePdfToolsSignatureValidation_SubIndication_ExpiredNoRevocationInformation     = 515,
    ePdfToolsSignatureValidation_SubIndication_Untrusted                          = 516,
    ePdfToolsSignatureValidation_SubIndication_Generic                            = 1024,
} TPdfToolsSignatureValidation_SubIndication;

typedef enum TPdfToolsSignatureValidation_SignatureSelector
{
    ePdfToolsSignatureValidation_SignatureSelector_Latest = 1,
    ePdfToolsSignatureValidation_SignatureSelector_All    = 2,
} TPdfToolsSignatureValidation_SignatureSelector;

typedef enum TPdfToolsSignatureValidation_TimeSource
{
    ePdfToolsSignatureValidation_TimeSource_ProofOfExistence = 0x0001,
    ePdfToolsSignatureValidation_TimeSource_ExpiredTimeStamp = 0x0002,
    ePdfToolsSignatureValidation_TimeSource_SignatureTime    = 0x0004,
} TPdfToolsSignatureValidation_TimeSource;

typedef enum TPdfToolsSignatureValidation_DataSource
{
    ePdfToolsSignatureValidation_DataSource_EmbedInSignature = 0x0001,
    ePdfToolsSignatureValidation_DataSource_EmbedInDocument  = 0x0002,
    ePdfToolsSignatureValidation_DataSource_Download         = 0x0004,
    ePdfToolsSignatureValidation_DataSource_System           = 0x0008,
    ePdfToolsSignatureValidation_DataSource_Aatl             = 0x0100,
    ePdfToolsSignatureValidation_DataSource_Eutl             = 0x0200,
    ePdfToolsSignatureValidation_DataSource_CustomTrustList  = 0x0400,
} TPdfToolsSignatureValidation_DataSource;

typedef enum TPdfToolsSignatureValidationProfiles_RevocationCheckPolicy
{
    ePdfToolsSignatureValidationProfiles_RevocationCheckPolicy_Required  = 1,
    ePdfToolsSignatureValidationProfiles_RevocationCheckPolicy_Supported = 2,
    ePdfToolsSignatureValidationProfiles_RevocationCheckPolicy_Optional  = 3,
    ePdfToolsSignatureValidationProfiles_RevocationCheckPolicy_NoCheck   = 4,
} TPdfToolsSignatureValidationProfiles_RevocationCheckPolicy;

typedef enum TPdfToolsPdf_OutputOptionsType
{
    ePdfToolsPdf_OutputOptionsType_OutputOptions,
    ePdfToolsPdf_OutputOptionsType_PdfToolsSign_OutputOptions
} TPdfToolsPdf_OutputOptionsType;

typedef enum TPdfToolsPdf_DocumentType
{
    ePdfToolsPdf_DocumentType_Document,
    ePdfToolsPdf_DocumentType_PdfToolsSign_PreparedDocument
} TPdfToolsPdf_DocumentType;

typedef enum TPdfToolsPdf_SignatureFieldType
{
    ePdfToolsPdf_SignatureFieldType_SignatureField,
    ePdfToolsPdf_SignatureFieldType_UnsignedSignatureField,
    ePdfToolsPdf_SignatureFieldType_SignedSignatureField,
    ePdfToolsPdf_SignatureFieldType_Signature,
    ePdfToolsPdf_SignatureFieldType_DocumentSignature,
    ePdfToolsPdf_SignatureFieldType_CertificationSignature,
    ePdfToolsPdf_SignatureFieldType_DocumentTimestamp
} TPdfToolsPdf_SignatureFieldType;

typedef enum TPdfToolsPdf_SignedSignatureFieldType
{
    ePdfToolsPdf_SignedSignatureFieldType_SignedSignatureField,
    ePdfToolsPdf_SignedSignatureFieldType_Signature,
    ePdfToolsPdf_SignedSignatureFieldType_DocumentSignature,
    ePdfToolsPdf_SignedSignatureFieldType_CertificationSignature,
    ePdfToolsPdf_SignedSignatureFieldType_DocumentTimestamp
} TPdfToolsPdf_SignedSignatureFieldType;

typedef enum TPdfToolsPdf_SignatureType
{
    ePdfToolsPdf_SignatureType_Signature,
    ePdfToolsPdf_SignatureType_DocumentSignature,
    ePdfToolsPdf_SignatureType_CertificationSignature
} TPdfToolsPdf_SignatureType;

typedef enum TPdfToolsImage_DocumentType
{
    ePdfToolsImage_DocumentType_Document,
    ePdfToolsImage_DocumentType_SinglePageDocument,
    ePdfToolsImage_DocumentType_MultiPageDocument
} TPdfToolsImage_DocumentType;

typedef enum TPdfToolsOptimizationProfiles_ProfileType
{
    ePdfToolsOptimizationProfiles_ProfileType_Profile,
    ePdfToolsOptimizationProfiles_ProfileType_Web,
    ePdfToolsOptimizationProfiles_ProfileType_Print,
    ePdfToolsOptimizationProfiles_ProfileType_Archive,
    ePdfToolsOptimizationProfiles_ProfileType_MinimalFileSize
} TPdfToolsOptimizationProfiles_ProfileType;

typedef enum TPdfToolsPdf2Image_ImageOptionsType
{
    ePdfToolsPdf2Image_ImageOptionsType_ImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_FaxImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_TiffJpegImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_TiffLzwImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_TiffFlateImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_PngImageOptions,
    ePdfToolsPdf2Image_ImageOptionsType_JpegImageOptions
} TPdfToolsPdf2Image_ImageOptionsType;

typedef enum TPdfToolsPdf2Image_ImageSectionMappingType
{
    ePdfToolsPdf2Image_ImageSectionMappingType_ImageSectionMapping,
    ePdfToolsPdf2Image_ImageSectionMappingType_RenderPageAsFax,
    ePdfToolsPdf2Image_ImageSectionMappingType_RenderPageAtResolution,
    ePdfToolsPdf2Image_ImageSectionMappingType_RenderPageToMaxImageSize
} TPdfToolsPdf2Image_ImageSectionMappingType;

typedef enum TPdfToolsPdf2ImageProfiles_ProfileType
{
    ePdfToolsPdf2ImageProfiles_ProfileType_Profile,
    ePdfToolsPdf2ImageProfiles_ProfileType_Fax,
    ePdfToolsPdf2ImageProfiles_ProfileType_Archive,
    ePdfToolsPdf2ImageProfiles_ProfileType_Viewing
} TPdfToolsPdf2ImageProfiles_ProfileType;

typedef enum TPdfToolsImage2Pdf_ImageMappingType
{
    ePdfToolsImage2Pdf_ImageMappingType_ImageMapping,
    ePdfToolsImage2Pdf_ImageMappingType_Auto,
    ePdfToolsImage2Pdf_ImageMappingType_ShrinkToPage,
    ePdfToolsImage2Pdf_ImageMappingType_ShrinkToFit,
    ePdfToolsImage2Pdf_ImageMappingType_ShrinkToPortrait
} TPdfToolsImage2Pdf_ImageMappingType;

typedef enum TPdfToolsImage2PdfProfiles_ProfileType
{
    ePdfToolsImage2PdfProfiles_ProfileType_Profile,
    ePdfToolsImage2PdfProfiles_ProfileType_Default,
    ePdfToolsImage2PdfProfiles_ProfileType_Archive
} TPdfToolsImage2PdfProfiles_ProfileType;

typedef enum TPdfToolsSign_SignatureConfigurationType
{
    ePdfToolsSign_SignatureConfigurationType_SignatureConfiguration,
    ePdfToolsSign_SignatureConfigurationType_PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration,
    ePdfToolsSign_SignatureConfigurationType_PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration,
    ePdfToolsSign_SignatureConfigurationType_PdfToolsCryptoProvidersPkcs11_SignatureConfiguration,
    ePdfToolsSign_SignatureConfigurationType_PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration
} TPdfToolsSign_SignatureConfigurationType;

typedef enum TPdfToolsSign_TimestampConfigurationType
{
    ePdfToolsSign_TimestampConfigurationType_TimestampConfiguration,
    ePdfToolsSign_TimestampConfigurationType_PdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration,
    ePdfToolsSign_TimestampConfigurationType_PdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration,
    ePdfToolsSign_TimestampConfigurationType_PdfToolsCryptoProvidersPkcs11_TimestampConfiguration,
    ePdfToolsSign_TimestampConfigurationType_PdfToolsCryptoProvidersBuiltIn_TimestampConfiguration
} TPdfToolsSign_TimestampConfigurationType;

typedef enum TPdfToolsCryptoProviders_ProviderType
{
    ePdfToolsCryptoProviders_ProviderType_Provider,
    ePdfToolsCryptoProviders_ProviderType_PdfToolsCryptoProvidersGlobalSignDss_Session,
    ePdfToolsCryptoProviders_ProviderType_PdfToolsCryptoProvidersSwisscomSigSrv_Session,
    ePdfToolsCryptoProviders_ProviderType_PdfToolsCryptoProvidersPkcs11_Session,
    ePdfToolsCryptoProviders_ProviderType_PdfToolsCryptoProvidersBuiltIn_Provider
} TPdfToolsCryptoProviders_ProviderType;

typedef enum TPdfToolsSignatureValidation_SignatureContentType
{
    ePdfToolsSignatureValidation_SignatureContentType_SignatureContent,
    ePdfToolsSignatureValidation_SignatureContentType_UnsupportedSignatureContent,
    ePdfToolsSignatureValidation_SignatureContentType_CmsSignatureContent,
    ePdfToolsSignatureValidation_SignatureContentType_TimeStampContent
} TPdfToolsSignatureValidation_SignatureContentType;

typedef enum TPdfToolsSignatureValidationProfiles_ProfileType
{
    ePdfToolsSignatureValidationProfiles_ProfileType_Profile,
    ePdfToolsSignatureValidationProfiles_ProfileType_Default
} TPdfToolsSignatureValidationProfiles_ProfileType;

typedef struct TPdfTools_ConsumptionData                       TPdfTools_ConsumptionData;
typedef struct TPdfTools_LicenseInfo                           TPdfTools_LicenseInfo;
typedef struct TPdfTools_Sdk                                   TPdfTools_Sdk;
typedef struct TPdfTools_StringList                            TPdfTools_StringList;
typedef struct TPdfTools_MetadataDictionary                    TPdfTools_MetadataDictionary;
typedef struct TPdfTools_HttpClientHandler                     TPdfTools_HttpClientHandler;
typedef struct TPdfToolsPdf_MetadataSettings                   TPdfToolsPdf_MetadataSettings;
typedef struct TPdfToolsPdf_Encryption                         TPdfToolsPdf_Encryption;
typedef struct TPdfToolsPdf_OutputOptions                      TPdfToolsPdf_OutputOptions;
typedef struct TPdfToolsPdf_Document                           TPdfToolsPdf_Document;
typedef struct TPdfToolsPdf_Metadata                           TPdfToolsPdf_Metadata;
typedef struct TPdfToolsPdf_SignatureField                     TPdfToolsPdf_SignatureField;
typedef struct TPdfToolsPdf_UnsignedSignatureField             TPdfToolsPdf_UnsignedSignatureField;
typedef struct TPdfToolsPdf_SignedSignatureField               TPdfToolsPdf_SignedSignatureField;
typedef struct TPdfToolsPdf_Signature                          TPdfToolsPdf_Signature;
typedef struct TPdfToolsPdf_DocumentSignature                  TPdfToolsPdf_DocumentSignature;
typedef struct TPdfToolsPdf_CertificationSignature             TPdfToolsPdf_CertificationSignature;
typedef struct TPdfToolsPdf_DocumentTimestamp                  TPdfToolsPdf_DocumentTimestamp;
typedef struct TPdfToolsPdf_SignatureFieldList                 TPdfToolsPdf_SignatureFieldList;
typedef struct TPdfToolsPdf_Revision                           TPdfToolsPdf_Revision;
typedef struct TPdfToolsImage_Page                             TPdfToolsImage_Page;
typedef struct TPdfToolsImage_PageList                         TPdfToolsImage_PageList;
typedef struct TPdfToolsImage_Document                         TPdfToolsImage_Document;
typedef struct TPdfToolsImage_SinglePageDocument               TPdfToolsImage_SinglePageDocument;
typedef struct TPdfToolsImage_MultiPageDocument                TPdfToolsImage_MultiPageDocument;
typedef struct TPdfToolsImage_DocumentList                     TPdfToolsImage_DocumentList;
typedef struct TPdfToolsDocumentAssembly_PageCopyOptions       TPdfToolsDocumentAssembly_PageCopyOptions;
typedef struct TPdfToolsDocumentAssembly_DocumentCopyOptions   TPdfToolsDocumentAssembly_DocumentCopyOptions;
typedef struct TPdfToolsDocumentAssembly_DocumentAssembler     TPdfToolsDocumentAssembly_DocumentAssembler;
typedef struct TPdfToolsOptimization_ImageRecompressionOptions TPdfToolsOptimization_ImageRecompressionOptions;
typedef struct TPdfToolsOptimization_FontOptions               TPdfToolsOptimization_FontOptions;
typedef struct TPdfToolsOptimization_RemovalOptions            TPdfToolsOptimization_RemovalOptions;
typedef struct TPdfToolsOptimization_Optimizer                 TPdfToolsOptimization_Optimizer;
typedef struct TPdfToolsOptimizationProfiles_Profile           TPdfToolsOptimizationProfiles_Profile;
typedef struct TPdfToolsOptimizationProfiles_Web               TPdfToolsOptimizationProfiles_Web;
typedef struct TPdfToolsOptimizationProfiles_Print             TPdfToolsOptimizationProfiles_Print;
typedef struct TPdfToolsOptimizationProfiles_Archive           TPdfToolsOptimizationProfiles_Archive;
typedef struct TPdfToolsOptimizationProfiles_MinimalFileSize   TPdfToolsOptimizationProfiles_MinimalFileSize;
typedef struct TPdfToolsPdf2Image_ContentOptions               TPdfToolsPdf2Image_ContentOptions;
typedef struct TPdfToolsPdf2Image_ImageOptions                 TPdfToolsPdf2Image_ImageOptions;
typedef struct TPdfToolsPdf2Image_FaxImageOptions              TPdfToolsPdf2Image_FaxImageOptions;
typedef struct TPdfToolsPdf2Image_TiffJpegImageOptions         TPdfToolsPdf2Image_TiffJpegImageOptions;
typedef struct TPdfToolsPdf2Image_TiffLzwImageOptions          TPdfToolsPdf2Image_TiffLzwImageOptions;
typedef struct TPdfToolsPdf2Image_TiffFlateImageOptions        TPdfToolsPdf2Image_TiffFlateImageOptions;
typedef struct TPdfToolsPdf2Image_PngImageOptions              TPdfToolsPdf2Image_PngImageOptions;
typedef struct TPdfToolsPdf2Image_JpegImageOptions             TPdfToolsPdf2Image_JpegImageOptions;
typedef struct TPdfToolsPdf2Image_ImageSectionMapping          TPdfToolsPdf2Image_ImageSectionMapping;
typedef struct TPdfToolsPdf2Image_RenderPageAsFax              TPdfToolsPdf2Image_RenderPageAsFax;
typedef struct TPdfToolsPdf2Image_RenderPageAtResolution       TPdfToolsPdf2Image_RenderPageAtResolution;
typedef struct TPdfToolsPdf2Image_RenderPageToMaxImageSize     TPdfToolsPdf2Image_RenderPageToMaxImageSize;
typedef struct TPdfToolsPdf2Image_Converter                    TPdfToolsPdf2Image_Converter;
typedef struct TPdfToolsPdf2ImageProfiles_Profile              TPdfToolsPdf2ImageProfiles_Profile;
typedef struct TPdfToolsPdf2ImageProfiles_Fax                  TPdfToolsPdf2ImageProfiles_Fax;
typedef struct TPdfToolsPdf2ImageProfiles_Archive              TPdfToolsPdf2ImageProfiles_Archive;
typedef struct TPdfToolsPdf2ImageProfiles_Viewing              TPdfToolsPdf2ImageProfiles_Viewing;
typedef struct TPdfToolsImage2Pdf_ImageMapping                 TPdfToolsImage2Pdf_ImageMapping;
typedef struct TPdfToolsImage2Pdf_Auto                         TPdfToolsImage2Pdf_Auto;
typedef struct TPdfToolsImage2Pdf_ShrinkToPage                 TPdfToolsImage2Pdf_ShrinkToPage;
typedef struct TPdfToolsImage2Pdf_ShrinkToFit                  TPdfToolsImage2Pdf_ShrinkToFit;
typedef struct TPdfToolsImage2Pdf_ShrinkToPortrait TPdfToolsImage2Pdf_ShrinkToPortrait; // Deprecated in Version 1.1.
typedef struct TPdfToolsImage2Pdf_ImageOptions     TPdfToolsImage2Pdf_ImageOptions;
typedef struct TPdfToolsImage2Pdf_Converter        TPdfToolsImage2Pdf_Converter;
typedef struct TPdfToolsImage2PdfProfiles_Profile  TPdfToolsImage2PdfProfiles_Profile;
typedef struct TPdfToolsImage2PdfProfiles_Default  TPdfToolsImage2PdfProfiles_Default;
typedef struct TPdfToolsImage2PdfProfiles_Archive  TPdfToolsImage2PdfProfiles_Archive;
typedef struct TPdfToolsPdfAValidation_Validator   TPdfToolsPdfAValidation_Validator;
typedef struct TPdfToolsPdfAValidation_ValidationOptions TPdfToolsPdfAValidation_ValidationOptions;
typedef struct TPdfToolsPdfAValidation_ValidationResult  TPdfToolsPdfAValidation_ValidationResult;
typedef struct TPdfToolsPdfAValidation_AnalysisOptions   TPdfToolsPdfAValidation_AnalysisOptions;
typedef struct TPdfToolsPdfAValidation_AnalysisResult    TPdfToolsPdfAValidation_AnalysisResult;
typedef struct TPdfToolsPdfAConversion_Converter         TPdfToolsPdfAConversion_Converter;
typedef struct TPdfToolsPdfAConversion_ConversionOptions TPdfToolsPdfAConversion_ConversionOptions;
typedef struct TPdfToolsSign_CustomTextVariableMap       TPdfToolsSign_CustomTextVariableMap;
typedef struct TPdfToolsSign_Appearance                  TPdfToolsSign_Appearance;
typedef struct TPdfToolsSign_SignatureConfiguration      TPdfToolsSign_SignatureConfiguration;
typedef struct TPdfToolsSign_TimestampConfiguration      TPdfToolsSign_TimestampConfiguration;
typedef struct TPdfToolsSign_OutputOptions               TPdfToolsSign_OutputOptions;
typedef struct TPdfToolsSign_MdpPermissionOptions        TPdfToolsSign_MdpPermissionOptions;
typedef struct TPdfToolsSign_SignatureFieldOptions       TPdfToolsSign_SignatureFieldOptions;
typedef struct TPdfToolsSign_PreparedDocument            TPdfToolsSign_PreparedDocument;
typedef struct TPdfToolsSign_Signer                      TPdfToolsSign_Signer;
typedef struct TPdfToolsCryptoProviders_Provider         TPdfToolsCryptoProviders_Provider;
typedef struct TPdfToolsCryptoProviders_Certificate      TPdfToolsCryptoProviders_Certificate;
typedef struct TPdfToolsCryptoProviders_CertificateList  TPdfToolsCryptoProviders_CertificateList;
typedef struct TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration;
typedef struct TPdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration
    TPdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration;
typedef struct TPdfToolsCryptoProvidersGlobalSignDss_Session TPdfToolsCryptoProvidersGlobalSignDss_Session;
typedef struct TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration;
typedef struct TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration
    TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration;
typedef struct TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp  TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp;
typedef struct TPdfToolsCryptoProvidersSwisscomSigSrv_Session TPdfToolsCryptoProvidersSwisscomSigSrv_Session;
typedef struct TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration;
typedef struct TPdfToolsCryptoProvidersPkcs11_TimestampConfiguration
                                                         TPdfToolsCryptoProvidersPkcs11_TimestampConfiguration;
typedef struct TPdfToolsCryptoProvidersPkcs11_Module     TPdfToolsCryptoProvidersPkcs11_Module;
typedef struct TPdfToolsCryptoProvidersPkcs11_Device     TPdfToolsCryptoProvidersPkcs11_Device;
typedef struct TPdfToolsCryptoProvidersPkcs11_Session    TPdfToolsCryptoProvidersPkcs11_Session;
typedef struct TPdfToolsCryptoProvidersPkcs11_DeviceList TPdfToolsCryptoProvidersPkcs11_DeviceList;
typedef struct TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration;
typedef struct TPdfToolsCryptoProvidersBuiltIn_TimestampConfiguration
                                                              TPdfToolsCryptoProvidersBuiltIn_TimestampConfiguration;
typedef struct TPdfToolsCryptoProvidersBuiltIn_Provider       TPdfToolsCryptoProvidersBuiltIn_Provider;
typedef struct TPdfToolsSignatureValidation_ConstraintResult  TPdfToolsSignatureValidation_ConstraintResult;
typedef struct TPdfToolsSignatureValidation_Validator         TPdfToolsSignatureValidation_Validator;
typedef struct TPdfToolsSignatureValidation_Certificate       TPdfToolsSignatureValidation_Certificate;
typedef struct TPdfToolsSignatureValidation_CertificateChain  TPdfToolsSignatureValidation_CertificateChain;
typedef struct TPdfToolsSignatureValidation_ValidationResults TPdfToolsSignatureValidation_ValidationResults;
typedef struct TPdfToolsSignatureValidation_ValidationResult  TPdfToolsSignatureValidation_ValidationResult;
typedef struct TPdfToolsSignatureValidation_SignatureContent  TPdfToolsSignatureValidation_SignatureContent;
typedef struct TPdfToolsSignatureValidation_UnsupportedSignatureContent
    TPdfToolsSignatureValidation_UnsupportedSignatureContent;
typedef struct TPdfToolsSignatureValidation_CmsSignatureContent TPdfToolsSignatureValidation_CmsSignatureContent;
typedef struct TPdfToolsSignatureValidation_TimeStampContent    TPdfToolsSignatureValidation_TimeStampContent;
typedef struct TPdfToolsSignatureValidation_CustomTrustList     TPdfToolsSignatureValidation_CustomTrustList;
typedef struct TPdfToolsSignatureValidationProfiles_Profile     TPdfToolsSignatureValidationProfiles_Profile;
typedef struct TPdfToolsSignatureValidationProfiles_ValidationOptions
    TPdfToolsSignatureValidationProfiles_ValidationOptions;
typedef struct TPdfToolsSignatureValidationProfiles_TrustConstraints
                                                            TPdfToolsSignatureValidationProfiles_TrustConstraints;
typedef struct TPdfToolsSignatureValidationProfiles_Default TPdfToolsSignatureValidationProfiles_Default;

typedef struct TPdfToolsGeomInt_Size
{
    int iWidth;
    int iHeight;
} TPdfToolsGeomInt_Size;

typedef struct TPdfToolsGeomUnits_Resolution
{
    double dXDpi;
    double dYDpi;
} TPdfToolsGeomUnits_Resolution;

typedef struct TPdfToolsGeomUnits_Size
{
    double dWidth;
    double dHeight;
} TPdfToolsGeomUnits_Size;

typedef struct TPdfToolsGeomUnits_Margin
{
    double dLeft;
    double dBottom;
    double dRight;
    double dTop;
} TPdfToolsGeomUnits_Margin;

typedef struct TPdfToolsGeomUnits_Point
{
    double dX;
    double dY;
} TPdfToolsGeomUnits_Point;

typedef struct TPdfToolsGeomUnits_Rectangle
{
    double dX;
    double dY;
    double dWidth;
    double dHeight;
} TPdfToolsGeomUnits_Rectangle;

typedef struct TPdfToolsSys_Date
{
    short iYear;
    short iMonth;
    short iDay;
    short iHour;
    short iMinute;
    short iSecond;
    short iTZSign;
    short iTZHour;
    short iTZMinute;
} TPdfToolsSys_Date;

struct TPdfToolsSys_StreamDescriptor;

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_TYPES_H__ */
