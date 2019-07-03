export module RecordTypes {
  export const A: RecordType = "A";
  export const AAAA: RecordType = "AAAA";
  export const ALIAS: RecordType = "ALIAS";
  export const CAA: RecordType = "CAA";
  export const CNAME: RecordType = "CNAME";
  export const HINFO: RecordType = "HINFO";
  export const MX: RecordType = "MX";
  export const NAPTR: RecordType = "NAPTR";
  export const NS: RecordType = "NS";
  export const POOL: RecordType = "POOL";
  export const PTR: RecordType = "PTR";
  export const SPF: RecordType = "SPF";
  export const SRV: RecordType = "SRV";
  export const SSHFP: RecordType = "SSHFP";
  export const TXT: RecordType = "TXT";
  export const URL: RecordType = "URL";
}

export type RecordType =
  | "A"
  | "AAAA"
  | "ALIAS"
  | "CAA"
  | "CNAME"
  | "HINFO"
  | "MX"
  | "NAPTR"
  | "NS"
  | "POOL"
  | "PTR"
  | "SPF"
  | "SRV"
  | "SSHFP"
  | "TXT"
  | "URL";
