/******************************************************************************
 *
 * File:            PdfTools_PdfToolsPdfAValidation.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSPDFAVALIDATION_H__
#define PDFTOOLS_PDFTOOLSPDFAVALIDATION_H__

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
#define TPdfToolsPdfAValidation_Validator_Error             TPdfToolsPdfAValidation_Validator_ErrorW
#define PdfToolsPdfAValidation_Validator_AddErrorHandler    PdfToolsPdfAValidation_Validator_AddErrorHandlerW
#define PdfToolsPdfAValidation_Validator_RemoveErrorHandler PdfToolsPdfAValidation_Validator_RemoveErrorHandlerW

#else
#define TPdfToolsPdfAValidation_Validator_Error             TPdfToolsPdfAValidation_Validator_ErrorA
#define PdfToolsPdfAValidation_Validator_AddErrorHandler    PdfToolsPdfAValidation_Validator_AddErrorHandlerA
#define PdfToolsPdfAValidation_Validator_RemoveErrorHandler PdfToolsPdfAValidation_Validator_RemoveErrorHandlerA

#endif

typedef void(PDFTOOLS_CALL* TPdfToolsPdfAValidation_Validator_ErrorA)(void* pContext, const char* szDataPart,
                                                                      const char*                           szMessage,
                                                                      TPdfToolsPdfAValidation_ErrorCategory iCategory,
                                                                      const char* szContext, int iPageNo,
                                                                      int iObjectNo);
typedef void(PDFTOOLS_CALL* TPdfToolsPdfAValidation_Validator_ErrorW)(void* pContext, const WCHAR* szDataPart,
                                                                      const WCHAR*                          szMessage,
                                                                      TPdfToolsPdfAValidation_ErrorCategory iCategory,
                                                                      const WCHAR* szContext, int iPageNo,
                                                                      int iObjectNo);

/******************************************************************************
 * Validator
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_AddErrorHandlerA(
    TPdfToolsPdfAValidation_Validator* pValidator, void* pContext, TPdfToolsPdfAValidation_Validator_ErrorA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_AddErrorHandlerW(
    TPdfToolsPdfAValidation_Validator* pValidator, void* pContext, TPdfToolsPdfAValidation_Validator_ErrorW pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_RemoveErrorHandlerA(
    TPdfToolsPdfAValidation_Validator* pValidator, void* pContext, TPdfToolsPdfAValidation_Validator_ErrorA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_RemoveErrorHandlerW(
    TPdfToolsPdfAValidation_Validator* pValidator, void* pContext, TPdfToolsPdfAValidation_Validator_ErrorW pFunction);

PDFTOOLS_EXPORT TPdfToolsPdfAValidation_Validator* PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_New(void);

PDFTOOLS_EXPORT TPdfToolsPdfAValidation_ValidationResult* PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_Validate(
    TPdfToolsPdfAValidation_Validator* pValidator, TPdfToolsPdf_Document* pDocument,
    TPdfToolsPdfAValidation_ValidationOptions* pOptions);
PDFTOOLS_EXPORT TPdfToolsPdfAValidation_AnalysisResult* PDFTOOLS_CALL PdfToolsPdfAValidation_Validator_Analyze(
    TPdfToolsPdfAValidation_Validator* pValidator, TPdfToolsPdf_Document* pDocument,
    TPdfToolsPdfAValidation_AnalysisOptions* pOptions);

/******************************************************************************
 * ValidationOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdfAValidation_ValidationOptions* PDFTOOLS_CALL
PdfToolsPdfAValidation_ValidationOptions_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_ValidationOptions_GetConformance(
    TPdfToolsPdfAValidation_ValidationOptions* pValidationOptions, TPdfToolsPdf_Conformance* pConformance);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_ValidationOptions_SetConformance(
    TPdfToolsPdfAValidation_ValidationOptions* pValidationOptions, const TPdfToolsPdf_Conformance* pConformance);

/******************************************************************************
 * ValidationResult
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL
PdfToolsPdfAValidation_ValidationResult_GetConformance(TPdfToolsPdfAValidation_ValidationResult* pValidationResult);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_ValidationResult_IsConforming(TPdfToolsPdfAValidation_ValidationResult* pValidationResult);

/******************************************************************************
 * AnalysisOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdfAValidation_AnalysisOptions* PDFTOOLS_CALL PdfToolsPdfAValidation_AnalysisOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisOptions_GetConformance(TPdfToolsPdfAValidation_AnalysisOptions* pAnalysisOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_AnalysisOptions_SetConformance(
    TPdfToolsPdfAValidation_AnalysisOptions* pAnalysisOptions, TPdfToolsPdf_Conformance iConformance);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisOptions_GetStrictMode(TPdfToolsPdfAValidation_AnalysisOptions* pAnalysisOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdfAValidation_AnalysisOptions_SetStrictMode(
    TPdfToolsPdfAValidation_AnalysisOptions* pAnalysisOptions, BOOL bStrictMode);

/******************************************************************************
 * AnalysisResult
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_GetConformance(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL PdfToolsPdfAValidation_AnalysisResult_GetRecommendedConformance(
    TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_IsConversionRecommended(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_IsConforming(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_IsSigned(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_GetHasEmbeddedFiles(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsPdfAValidation_AnalysisResult_GetFontCount(TPdfToolsPdfAValidation_AnalysisResult* pAnalysisResult);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSPDFAVALIDATION_H__ */
