import axios from "axios";
import fs from "fs";
import path from "path";
import FormData from "form-data";
import configuration from "../config/config.json"; // your config file

export interface TokenResponse {
  result: {
    token: string;
  };
}

export interface UploadResponse {
  result?: {
    file?: {
      name: string;
      url: string;
    };
  };
  error?: string;
}

/**
 * Normalize hostname for pCloudy API.
 * Returns 'device.pcloudy.com' for known regional hosts,
 * otherwise returns the original hostname from config.
 */
function getPCloudyHost(): string {
  const knownRegions = [
    "ind-west.pcloudy.com",
    "us.pcloudy.com",
    "sg.pcloudy.com",
    "uae.pcloudy.com"
  ];

  const host = configuration.hostname;
  return knownRegions.includes(host) ? "device.pcloudy.com" : host;
}

export async function getToken(username: string, password: string): Promise<TokenResponse | { error: string }> {
  try {
    const host = getPCloudyHost();
    const response = await axios.get(`https://${host}/api/access`, {
      auth: { username, password },
    });
    return response.data;
  } catch (err: any) {
    return { error: err.message };
  }
}

export async function uploadApp(
  filePath: string,
  filterValue = "all",
  username: string,
  password: string
): Promise<UploadResponse> {
  try {
    const tokenData = await getToken(username, password);
    if ("error" in tokenData) {
      throw new Error(`Token fetch failed: ${tokenData.error}`);
    }

    const token = tokenData.result.token;
    const filePathResolved = path.resolve(filePath);

    if (!fs.existsSync(filePathResolved)) {
      throw new Error(`Path does not exist: '${filePath}'`);
    }

    const formData = new FormData();
    formData.append("file", fs.createReadStream(filePathResolved), path.basename(filePathResolved));
    formData.append("source_type", "raw");
    formData.append("token", token);
    formData.append("filter", filterValue);

    const host = getPCloudyHost();
    const response = await axios.post(`https://${host}/api/upload_file`, formData, {
      headers: { ...formData.getHeaders() },
    });

    if (response.data?.error) {
      throw new Error(`Upload failed: ${response.data.error}`);
    }

    return response.data as UploadResponse;
  } catch (err: any) {
    throw new Error(`UploadApp failed: ${err.message}`);
  }
}
