/******************************************************************************
 *
 * File:            PdfTools_PdfToolsImage.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSIMAGE_H__
#define PDFTOOLS_PDFTOOLSIMAGE_H__

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
 * Page
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage_Page_GetSize(TPdfToolsImage_Page* pPage, TPdfToolsGeomInt_Size* pSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage_Page_GetResolution(TPdfToolsImage_Page*           pPage,
                                                                    TPdfToolsGeomUnits_Resolution* pResolution);

/******************************************************************************
 * PageList
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL                  PdfToolsImage_PageList_GetCount(TPdfToolsImage_PageList* pPageList);
PDFTOOLS_EXPORT TPdfToolsImage_Page* PDFTOOLS_CALL PdfToolsImage_PageList_Get(TPdfToolsImage_PageList* pPageList,
                                                                              int                      iIndex);

/******************************************************************************
 * Document
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage_Document* PDFTOOLS_CALL
PdfToolsImage_Document_Open(const TPdfToolsSys_StreamDescriptor* pStreamDesc);

PDFTOOLS_EXPORT TPdfToolsImage_DocumentType PDFTOOLS_CALL
                                   PdfToolsImage_Document_GetType(TPdfToolsImage_Document* pDocument);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage_Document_Close(TPdfToolsImage_Document* pObject);
/******************************************************************************
 * SinglePageDocument
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage_Page* PDFTOOLS_CALL
PdfToolsImage_SinglePageDocument_GetPage(TPdfToolsImage_SinglePageDocument* pSinglePageDocument);

/******************************************************************************
 * MultiPageDocument
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage_PageList* PDFTOOLS_CALL
PdfToolsImage_MultiPageDocument_GetPages(TPdfToolsImage_MultiPageDocument* pMultiPageDocument);

/******************************************************************************
 * DocumentList
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage_DocumentList* PDFTOOLS_CALL PdfToolsImage_DocumentList_New(void);

PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfToolsImage_DocumentList_GetCount(TPdfToolsImage_DocumentList* pDocumentList);
PDFTOOLS_EXPORT TPdfToolsImage_Document* PDFTOOLS_CALL
PdfToolsImage_DocumentList_Get(TPdfToolsImage_DocumentList* pDocumentList, int iIndex);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage_DocumentList_Add(TPdfToolsImage_DocumentList* pDocumentList,
                                                                  TPdfToolsImage_Document*     pDocument);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSIMAGE_H__ */
