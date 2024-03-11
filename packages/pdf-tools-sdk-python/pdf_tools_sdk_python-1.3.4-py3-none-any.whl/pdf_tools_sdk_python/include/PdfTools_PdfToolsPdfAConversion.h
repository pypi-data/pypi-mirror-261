/******************************************************************************
 *
 * File:            PdfTools_PdfToolsPdfAConversion.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSPDFACONVERSION_H__
#define PDFTOOLS_PDFTOOLSPDFACONVERSION_H__

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
#define TPdfToolsPdfAConversion_Converter_ConversionEvent TPdfToolsPdfAConversion_Converter_ConversionEventW
#define PdfToolsPdfAConversion_Converter_AddConversionEventHandler \
    PdfToolsPdfAConversion_Converter_AddConversionEventHandlerW
#define PdfToolsPdfAConversion_Converter_RemoveConversionEventHandler \
    PdfToolsPdfAConversion_Converter_RemoveConversionEventHandlerW

#else
#define TPdfToolsPdfAConversion_Converter_ConversionEvent TPdfToolsPdfAConversion_Converter_ConversionEventA
#define PdfToolsPdfAConversion_Converter_AddConversionEventHandler \
    PdfToolsPdfAConversion_Converter_AddConversionEventHandlerA
#define PdfToolsPdfAConversion_Converter_RemoveConversionEventHandler \
    PdfToolsPdfAConversion_Converter_RemoveConversionEventHandlerA

#endif

typedef void(PDFTOOLS_CALL* TPdfToolsPdfAConversion_Converter_ConversionEventA)(
    void* pContext, const char* szDataPart, const char* szMessage, TPdfToolsPdfAConversion_EventSeverity iSeverity,
    TPdfToolsPdfAConversion_EventCategory iCategory, TPdfToolsPdfAConversion_EventCode iCode, const char* szContext,
    int iPageNo);
typedef void(PDFTOOLS_CALL* TPdfToolsPdfAConversion_Converter_ConversionEventW)(
    void* pContext, const WCHAR* szDataPart, const WCHAR* szMessage, TPdfToolsPdfAConversion_EventSeverity iSeverity,
    TPdfToolsPdfAConversion_EventCategory iCategory, TPdfToolsPdfAConversion_EventCode iCode, const WCHAR* szContext,
    int iPageNo);

/******************************************************************************
 * Converter
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_AddConversionEventHandlerA(
    TPdfToolsPdfAConversion_Converter* pConverter, void* pContext,
    TPdfToolsPdfAConversion_Converter_ConversionEventA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_AddConversionEventHandlerW(
    TPdfToolsPdfAConversion_Converter* pConverter, void* pContext,
    TPdfToolsPdfAConversion_Converter_ConversionEventW pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_RemoveConversionEventHandlerA(
    TPdfToolsPdfAConversion_Converter* pConverter, void* pContext,
    TPdfToolsPdfAConversion_Converter_ConversionEventA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_RemoveConversionEventHandlerW(
    TPdfToolsPdfAConversion_Converter* pConverter, void* pContext,
    TPdfToolsPdfAConversion_Converter_ConversionEventW pFunction);

PDFTOOLS_EXPORT TPdfToolsPdfAConversion_Converter* PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsPdfAConversion_Converter_Convert(
    TPdfToolsPdfAConversion_Converter* pConverter, TPdfToolsPdfAValidation_AnalysisResult* pAnalysis,
    TPdfToolsPdf_Document* pDocument, const TPdfToolsSys_StreamDescriptor* pOutStreamDesc,
    TPdfToolsPdfAConversion_ConversionOptions* pOptions, TPdfToolsPdf_OutputOptions* pOutOptions);

/******************************************************************************
 * ConversionOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdfAConversion_ConversionOptions* PDFTOOLS_CALL
PdfToolsPdfAConversion_ConversionOptions_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_ConversionOptions_GetConformance(
    TPdfToolsPdfAConversion_ConversionOptions* pConversionOptions, TPdfToolsPdf_Conformance* pConformance);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_ConversionOptions_SetConformance(
    TPdfToolsPdfAConversion_ConversionOptions* pConversionOptions, const TPdfToolsPdf_Conformance* pConformance);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAConversion_ConversionOptions_GetCopyMetadata(TPdfToolsPdfAConversion_ConversionOptions* pConversionOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAConversion_ConversionOptions_SetCopyMetadata(
    TPdfToolsPdfAConversion_ConversionOptions* pConversionOptions, BOOL bCopyMetadata);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSPDFACONVERSION_H__ */
