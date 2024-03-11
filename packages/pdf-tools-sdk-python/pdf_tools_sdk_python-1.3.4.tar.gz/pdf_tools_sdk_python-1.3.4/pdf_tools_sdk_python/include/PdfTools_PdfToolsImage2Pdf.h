/******************************************************************************
 *
 * File:            PdfTools_PdfToolsImage2Pdf.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSIMAGE2PDF_H__
#define PDFTOOLS_PDFTOOLSIMAGE2PDF_H__

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

PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ImageMappingType PDFTOOLS_CALL
PdfToolsImage2Pdf_ImageMapping_GetType(TPdfToolsImage2Pdf_ImageMapping* pImageMapping);
/******************************************************************************
 * Auto
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_Auto* PDFTOOLS_CALL PdfToolsImage2Pdf_Auto_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_Auto_GetMaxPageSize(TPdfToolsImage2Pdf_Auto* pAuto,
                                                                         TPdfToolsGeomUnits_Size* pMaxPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_Auto_SetMaxPageSize(TPdfToolsImage2Pdf_Auto*       pAuto,
                                                                         const TPdfToolsGeomUnits_Size* pMaxPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_Auto_GetDefaultPageMargin(
    TPdfToolsImage2Pdf_Auto* pAuto, TPdfToolsGeomUnits_Margin* pDefaultPageMargin);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_Auto_SetDefaultPageMargin(
    TPdfToolsImage2Pdf_Auto* pAuto, const TPdfToolsGeomUnits_Margin* pDefaultPageMargin);

/******************************************************************************
 * ShrinkToPage
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ShrinkToPage* PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPage_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPage_GetPageSize(
    TPdfToolsImage2Pdf_ShrinkToPage* pShrinkToPage, TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPage_SetPageSize(
    TPdfToolsImage2Pdf_ShrinkToPage* pShrinkToPage, const TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPage_GetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToPage* pShrinkToPage, TPdfToolsGeomUnits_Margin* pPageMargin);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPage_SetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToPage* pShrinkToPage, const TPdfToolsGeomUnits_Margin* pPageMargin);

/******************************************************************************
 * ShrinkToFit
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ShrinkToFit* PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToFit_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToFit_GetPageSize(
    TPdfToolsImage2Pdf_ShrinkToFit* pShrinkToFit, TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToFit_SetPageSize(
    TPdfToolsImage2Pdf_ShrinkToFit* pShrinkToFit, const TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToFit_GetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToFit* pShrinkToFit, TPdfToolsGeomUnits_Margin* pPageMargin);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToFit_SetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToFit* pShrinkToFit, const TPdfToolsGeomUnits_Margin* pPageMargin);

/******************************************************************************
 * ShrinkToPortrait
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ShrinkToPortrait* PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPortrait_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPortrait_GetPageSize(
    TPdfToolsImage2Pdf_ShrinkToPortrait* pShrinkToPortrait, TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPortrait_SetPageSize(
    TPdfToolsImage2Pdf_ShrinkToPortrait* pShrinkToPortrait, const TPdfToolsGeomUnits_Size* pPageSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPortrait_GetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToPortrait* pShrinkToPortrait, TPdfToolsGeomUnits_Margin* pPageMargin);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ShrinkToPortrait_SetPageMargin(
    TPdfToolsImage2Pdf_ShrinkToPortrait* pShrinkToPortrait, const TPdfToolsGeomUnits_Margin* pPageMargin);

/******************************************************************************
 * ImageOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ImageMapping* PDFTOOLS_CALL
PdfToolsImage2Pdf_ImageOptions_GetMapping(TPdfToolsImage2Pdf_ImageOptions* pImageOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2Pdf_ImageOptions_SetMapping(
    TPdfToolsImage2Pdf_ImageOptions* pImageOptions, TPdfToolsImage2Pdf_ImageMapping* pMapping);

/******************************************************************************
 * Converter
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_Converter* PDFTOOLS_CALL PdfToolsImage2Pdf_Converter_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsImage2Pdf_Converter_Convert(
    TPdfToolsImage2Pdf_Converter* pConverter, TPdfToolsImage_Document* pImage,
    const TPdfToolsSys_StreamDescriptor* pOutStreamDesc, TPdfToolsImage2PdfProfiles_Profile* pProfile,
    TPdfToolsPdf_OutputOptions* pOutOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsImage2Pdf_Converter_ConvertMultiple(
    TPdfToolsImage2Pdf_Converter* pConverter, TPdfToolsImage_DocumentList* pImages,
    const TPdfToolsSys_StreamDescriptor* pOutStreamDesc, TPdfToolsImage2PdfProfiles_Profile* pProfile,
    TPdfToolsPdf_OutputOptions* pOutOptions);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSIMAGE2PDF_H__ */
