/******************************************************************************
 *
 * File:            PdfTools_PdfToolsOptimization.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSOPTIMIZATION_H__
#define PDFTOOLS_PDFTOOLSOPTIMIZATION_H__

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
 * ImageRecompressionOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimization_CompressionAlgorithmSelection PDFTOOLS_CALL
PdfToolsOptimization_ImageRecompressionOptions_GetAlgorithmSelection(
    TPdfToolsOptimization_ImageRecompressionOptions* pImageRecompressionOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_ImageRecompressionOptions_SetAlgorithmSelection(
    TPdfToolsOptimization_ImageRecompressionOptions*    pImageRecompressionOptions,
    TPdfToolsOptimization_CompressionAlgorithmSelection iAlgorithmSelection);
PDFTOOLS_EXPORT double PDFTOOLS_CALL PdfToolsOptimization_ImageRecompressionOptions_GetCompressionQuality(
    TPdfToolsOptimization_ImageRecompressionOptions* pImageRecompressionOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_ImageRecompressionOptions_SetCompressionQuality(
    TPdfToolsOptimization_ImageRecompressionOptions* pImageRecompressionOptions, double dCompressionQuality);

/******************************************************************************
 * FontOptions
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_FontOptions_GetMerge(TPdfToolsOptimization_FontOptions* pFontOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_FontOptions_SetMerge(TPdfToolsOptimization_FontOptions* pFontOptions, BOOL bMerge);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_FontOptions_GetRemoveStandardFonts(TPdfToolsOptimization_FontOptions* pFontOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_FontOptions_SetRemoveStandardFonts(
    TPdfToolsOptimization_FontOptions* pFontOptions, BOOL bRemoveStandardFonts);

/******************************************************************************
 * RemovalOptions
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveAlternateImages(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveAlternateImages(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveAlternateImages);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveArticleThreads(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveArticleThreads(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveArticleThreads);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveMetadata(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveMetadata(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveMetadata);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveOutputIntents(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveOutputIntents(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveOutputIntents);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemovePieceInfo(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemovePieceInfo(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemovePieceInfo);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveStructureTree(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveStructureTree(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveStructureTree);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveThumbnails(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveThumbnails(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, BOOL bRemoveThumbnails);
PDFTOOLS_EXPORT TPdfToolsOptimization_RemovalStrategy PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetRemoveSignatureAppearances(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetRemoveSignatureAppearances(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions,
    TPdfToolsOptimization_RemovalStrategy iRemoveSignatureAppearances);
PDFTOOLS_EXPORT TPdfToolsOptimization_ConversionStrategy PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetAnnotations(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetAnnotations(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, TPdfToolsOptimization_ConversionStrategy iAnnotations);
PDFTOOLS_EXPORT TPdfToolsOptimization_ConversionStrategy PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetFormFields(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetFormFields(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, TPdfToolsOptimization_ConversionStrategy iFormFields);
PDFTOOLS_EXPORT TPdfToolsOptimization_ConversionStrategy PDFTOOLS_CALL
PdfToolsOptimization_RemovalOptions_GetLinks(TPdfToolsOptimization_RemovalOptions* pRemovalOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimization_RemovalOptions_SetLinks(
    TPdfToolsOptimization_RemovalOptions* pRemovalOptions, TPdfToolsOptimization_ConversionStrategy iLinks);

/******************************************************************************
 * Optimizer
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimization_Optimizer* PDFTOOLS_CALL PdfToolsOptimization_Optimizer_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsOptimization_Optimizer_OptimizeDocument(
    TPdfToolsOptimization_Optimizer* pOptimizer, TPdfToolsPdf_Document* pInDoc,
    const TPdfToolsSys_StreamDescriptor* pOutStreamDesc, TPdfToolsOptimizationProfiles_Profile* pProfile,
    TPdfToolsPdf_OutputOptions* pOutOptions);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSOPTIMIZATION_H__ */
