# SonarQube API Handler
*created: 2024/07/11*

## Overview
**For retrieving a list of issues and security hotspots from SonarQube**

This tool converts JSON data files into an Excel file. It also combines multiple data files into a single Excel file.

## Supported SonarQube APIs
- Issues: `api/issues/search`
- Security Hotspots: `api/hotspots/search`

For additional information on the SonarQube API, please refer to the [SonarQube Web API documentation](https://next.sonarqube.com/sonarqube/web_api).

## File Naming Convention
Naming convention for JSON data files:
- Format: `<module_name>-<data_type>.json`
- Examples: `ptinvest-issues.json`, `ptinvest-hotspots.json`

(`data_type` only supports `issues` and `hotspots`)

## Important Note
> Due to error from SonarQube side, direct API calls from the application are currently not supported. As a workaround, please manually execute the API requests through your web browser and save the resulting JSON data files into the `input-json-data` folder.

> **Note: Calling API part is not implemented completely.**
