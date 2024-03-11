/******************************************************************************
 *
 * File:            PdfTools_PdfToolsDocumentAssembly.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSDOCUMENTASSEMBLY_H__
#define PDFTOOLS_PDFTOOLSDOCUMENTASSEMBLY_H__

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
 * PageCopyOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_PageCopyOptions* PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_CopyStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetLinks(TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetLinks(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, TPdfToolsDocumentAssembly_CopyStrategy iLinks);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_CopyStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetFormFields(TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetFormFields(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, TPdfToolsDocumentAssembly_CopyStrategy iFormFields);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_RemovalStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetSignedSignatures(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetSignedSignatures(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions,
    TPdfToolsDocumentAssembly_RemovalStrategy  iSignedSignatures);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_CopyStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetUnsignedSignatures(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetUnsignedSignatures(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions,
    TPdfToolsDocumentAssembly_CopyStrategy     iUnsignedSignatures);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_CopyStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetAnnotations(TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetAnnotations(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, TPdfToolsDocumentAssembly_CopyStrategy iAnnotations);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_GetCopyOutlineItems(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetCopyOutlineItems(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, BOOL bCopyOutlineItems);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_GetCopyAssociatedFiles(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetCopyAssociatedFiles(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, BOOL bCopyAssociatedFiles);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_GetCopyLogicalStructure(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetCopyLogicalStructure(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, BOOL bCopyLogicalStructure);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_NameConflictResolution PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetFormFieldConflictResolution(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetFormFieldConflictResolution(
    TPdfToolsDocumentAssembly_PageCopyOptions*       pPageCopyOptions,
    TPdfToolsDocumentAssembly_NameConflictResolution iFormFieldConflictResolution);
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_NamedDestinationCopyStrategy PDFTOOLS_CALL
PdfToolsDocumentAssembly_PageCopyOptions_GetNamedDestinations(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetNamedDestinations(
    TPdfToolsDocumentAssembly_PageCopyOptions*             pPageCopyOptions,
    TPdfToolsDocumentAssembly_NamedDestinationCopyStrategy iNamedDestinations);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_GetOptimizeResources(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_PageCopyOptions_SetOptimizeResources(
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions, BOOL bOptimizeResources);

/******************************************************************************
 * DocumentCopyOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_DocumentCopyOptions* PDFTOOLS_CALL
PdfToolsDocumentAssembly_DocumentCopyOptions_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_GetCopyMetadata(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_SetCopyMetadata(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions, BOOL bCopyMetadata);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_GetCopyOutputIntent(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_SetCopyOutputIntent(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions, BOOL bCopyOutputIntent);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_GetCopyViewerSettings(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_SetCopyViewerSettings(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions, BOOL bCopyViewerSettings);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_GetCopyEmbeddedFiles(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentCopyOptions_SetCopyEmbeddedFiles(
    TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions, BOOL bCopyEmbeddedFiles);

/******************************************************************************
 * DocumentAssembler
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsDocumentAssembly_DocumentAssembler* PDFTOOLS_CALL
PdfToolsDocumentAssembly_DocumentAssembler_New(const TPdfToolsSys_StreamDescriptor* pOutStreamDesc,
                                               TPdfToolsPdf_OutputOptions*          pOutOptions,
                                               const TPdfToolsPdf_Conformance*      pConformance);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsDocumentAssembly_DocumentAssembler_Append(
    TPdfToolsDocumentAssembly_DocumentAssembler* pDocumentAssembler, TPdfToolsPdf_Document* pInDoc,
    const int* pFirstPage, const int* pLastPage, TPdfToolsDocumentAssembly_DocumentCopyOptions* pDocumentCopyOptions,
    TPdfToolsDocumentAssembly_PageCopyOptions* pPageCopyOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL
PdfToolsDocumentAssembly_DocumentAssembler_Assemble(TPdfToolsDocumentAssembly_DocumentAssembler* pDocumentAssembler);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsDocumentAssembly_DocumentAssembler_Close(TPdfToolsDocumentAssembly_DocumentAssembler* pObject);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSDOCUMENTASSEMBLY_H__ */
