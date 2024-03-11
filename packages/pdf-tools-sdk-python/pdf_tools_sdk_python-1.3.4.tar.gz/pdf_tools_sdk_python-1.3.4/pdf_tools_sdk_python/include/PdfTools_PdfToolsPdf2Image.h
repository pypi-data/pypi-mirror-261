/******************************************************************************
 *
 * File:            PdfTools_PdfToolsPdf2Image.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSPDF2IMAGE_H__
#define PDFTOOLS_PDFTOOLSPDF2IMAGE_H__

#ifndef PDFTOOLS_CALL
#if defined(WIN32)
#define PDFTOOLS_CALL __stdcall
#else
#define PDFTOOLS_CALL
#endif
#endif

#include "PdfTools_Types.h"
#include "PdfTools_PdfToolsSys.h"

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _UNICODE
#else
#endif

/******************************************************************************
 * ContentOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_AnnotationOptions PDFTOOLS_CALL
PdfToolsPdf2Image_ContentOptions_GetAnnotations(TPdfToolsPdf2Image_ContentOptions* pContentOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_ContentOptions_SetAnnotations(
    TPdfToolsPdf2Image_ContentOptions* pContentOptions, TPdfToolsPdf2Image_AnnotationOptions iAnnotations);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_ImageOptionsType PDFTOOLS_CALL
PdfToolsPdf2Image_ImageOptions_GetType(TPdfToolsPdf2Image_ImageOptions* pImageOptions);
/******************************************************************************
 * FaxImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_FaxVerticalResolution PDFTOOLS_CALL
PdfToolsPdf2Image_FaxImageOptions_GetVerticalResolution(TPdfToolsPdf2Image_FaxImageOptions* pFaxImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_FaxImageOptions_SetVerticalResolution(
    TPdfToolsPdf2Image_FaxImageOptions* pFaxImageOptions, TPdfToolsPdf2Image_FaxVerticalResolution iVerticalResolution);
PDFTOOLS_EXPORT TPdfToolsPdf2Image_TiffBitonalCompressionType PDFTOOLS_CALL
PdfToolsPdf2Image_FaxImageOptions_GetCompression(TPdfToolsPdf2Image_FaxImageOptions* pFaxImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_FaxImageOptions_SetCompression(
    TPdfToolsPdf2Image_FaxImageOptions* pFaxImageOptions, TPdfToolsPdf2Image_TiffBitonalCompressionType iCompression);

/******************************************************************************
 * TiffJpegImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_TiffJpegImageOptions* PDFTOOLS_CALL PdfToolsPdf2Image_TiffJpegImageOptions_New(void);

PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsPdf2Image_TiffJpegImageOptions_GetJpegQuality(TPdfToolsPdf2Image_TiffJpegImageOptions* pTiffJpegImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffJpegImageOptions_SetJpegQuality(
    TPdfToolsPdf2Image_TiffJpegImageOptions* pTiffJpegImageOptions, int iJpegQuality);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffJpegImageOptions_GetColorSpace(
    TPdfToolsPdf2Image_TiffJpegImageOptions* pTiffJpegImageOptions, TPdfToolsPdf2Image_JpegColorSpace* pColorSpace);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf2Image_TiffJpegImageOptions_SetColorSpace(TPdfToolsPdf2Image_TiffJpegImageOptions* pTiffJpegImageOptions,
                                                     const TPdfToolsPdf2Image_JpegColorSpace* pColorSpace);

/******************************************************************************
 * TiffLzwImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_TiffLzwImageOptions* PDFTOOLS_CALL PdfToolsPdf2Image_TiffLzwImageOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_BackgroundType PDFTOOLS_CALL
PdfToolsPdf2Image_TiffLzwImageOptions_GetBackground(TPdfToolsPdf2Image_TiffLzwImageOptions* pTiffLzwImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffLzwImageOptions_SetBackground(
    TPdfToolsPdf2Image_TiffLzwImageOptions* pTiffLzwImageOptions, TPdfToolsPdf2Image_BackgroundType iBackground);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffLzwImageOptions_GetColorSpace(
    TPdfToolsPdf2Image_TiffLzwImageOptions* pTiffLzwImageOptions, TPdfToolsPdf2Image_ColorSpace* pColorSpace);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffLzwImageOptions_SetColorSpace(
    TPdfToolsPdf2Image_TiffLzwImageOptions* pTiffLzwImageOptions, const TPdfToolsPdf2Image_ColorSpace* pColorSpace);

/******************************************************************************
 * TiffFlateImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_TiffFlateImageOptions* PDFTOOLS_CALL
PdfToolsPdf2Image_TiffFlateImageOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_BackgroundType PDFTOOLS_CALL
PdfToolsPdf2Image_TiffFlateImageOptions_GetBackground(TPdfToolsPdf2Image_TiffFlateImageOptions* pTiffFlateImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffFlateImageOptions_SetBackground(
    TPdfToolsPdf2Image_TiffFlateImageOptions* pTiffFlateImageOptions, TPdfToolsPdf2Image_BackgroundType iBackground);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffFlateImageOptions_GetColorSpace(
    TPdfToolsPdf2Image_TiffFlateImageOptions* pTiffFlateImageOptions, TPdfToolsPdf2Image_ColorSpace* pColorSpace);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_TiffFlateImageOptions_SetColorSpace(
    TPdfToolsPdf2Image_TiffFlateImageOptions* pTiffFlateImageOptions, const TPdfToolsPdf2Image_ColorSpace* pColorSpace);

/******************************************************************************
 * PngImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_PngImageOptions* PDFTOOLS_CALL PdfToolsPdf2Image_PngImageOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_BackgroundType PDFTOOLS_CALL
PdfToolsPdf2Image_PngImageOptions_GetBackground(TPdfToolsPdf2Image_PngImageOptions* pPngImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_PngImageOptions_SetBackground(
    TPdfToolsPdf2Image_PngImageOptions* pPngImageOptions, TPdfToolsPdf2Image_BackgroundType iBackground);
PDFTOOLS_EXPORT TPdfToolsPdf2Image_PngColorSpace PDFTOOLS_CALL
PdfToolsPdf2Image_PngImageOptions_GetColorSpace(TPdfToolsPdf2Image_PngImageOptions* pPngImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_PngImageOptions_SetColorSpace(
    TPdfToolsPdf2Image_PngImageOptions* pPngImageOptions, TPdfToolsPdf2Image_PngColorSpace iColorSpace);

/******************************************************************************
 * JpegImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_JpegImageOptions* PDFTOOLS_CALL PdfToolsPdf2Image_JpegImageOptions_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_JpegImageOptions_GetColorSpace(
    TPdfToolsPdf2Image_JpegImageOptions* pJpegImageOptions, TPdfToolsPdf2Image_JpegColorSpace* pColorSpace);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_JpegImageOptions_SetColorSpace(
    TPdfToolsPdf2Image_JpegImageOptions* pJpegImageOptions, const TPdfToolsPdf2Image_JpegColorSpace* pColorSpace);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsPdf2Image_JpegImageOptions_GetJpegQuality(TPdfToolsPdf2Image_JpegImageOptions* pJpegImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_JpegImageOptions_SetJpegQuality(
    TPdfToolsPdf2Image_JpegImageOptions* pJpegImageOptions, int iJpegQuality);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_ImageSectionMappingType PDFTOOLS_CALL
PdfToolsPdf2Image_ImageSectionMapping_GetType(TPdfToolsPdf2Image_ImageSectionMapping* pImageSectionMapping);
/******************************************************************************
 * RenderPageAtResolution
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_RenderPageAtResolution* PDFTOOLS_CALL
PdfToolsPdf2Image_RenderPageAtResolution_New(const TPdfToolsGeomUnits_Resolution* pResolution);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_RenderPageAtResolution_GetResolution(
    TPdfToolsPdf2Image_RenderPageAtResolution* pRenderPageAtResolution, TPdfToolsGeomUnits_Resolution* pResolution);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_RenderPageAtResolution_SetResolution(
    TPdfToolsPdf2Image_RenderPageAtResolution* pRenderPageAtResolution,
    const TPdfToolsGeomUnits_Resolution*       pResolution);

/******************************************************************************
 * RenderPageToMaxImageSize
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_RenderPageToMaxImageSize* PDFTOOLS_CALL
PdfToolsPdf2Image_RenderPageToMaxImageSize_New(const TPdfToolsGeomInt_Size* pSize);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_RenderPageToMaxImageSize_GetSize(
    TPdfToolsPdf2Image_RenderPageToMaxImageSize* pRenderPageToMaxImageSize, TPdfToolsGeomInt_Size* pSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2Image_RenderPageToMaxImageSize_SetSize(
    TPdfToolsPdf2Image_RenderPageToMaxImageSize* pRenderPageToMaxImageSize, const TPdfToolsGeomInt_Size* pSize);

/******************************************************************************
 * Converter
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2Image_Converter* PDFTOOLS_CALL PdfToolsPdf2Image_Converter_New(void);

PDFTOOLS_EXPORT TPdfToolsImage_MultiPageDocument* PDFTOOLS_CALL PdfToolsPdf2Image_Converter_ConvertDocument(
    TPdfToolsPdf2Image_Converter* pConverter, TPdfToolsPdf_Document* pInDoc,
    const TPdfToolsSys_StreamDescriptor* pOutStreamDesc, TPdfToolsPdf2ImageProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsImage_Document* PDFTOOLS_CALL PdfToolsPdf2Image_Converter_ConvertPage(
    TPdfToolsPdf2Image_Converter* pConverter, TPdfToolsPdf_Document* pInDoc,
    const TPdfToolsSys_StreamDescriptor* pOutStreamDesc, TPdfToolsPdf2ImageProfiles_Profile* pProfile, int iPageNumber);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSPDF2IMAGE_H__ */
