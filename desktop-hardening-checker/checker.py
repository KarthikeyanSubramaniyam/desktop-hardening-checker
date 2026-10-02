"""Read-only desktop hardening checks using an exported JSON posture snapshot."""
import argparse, json

CHECKS={"firewall_enabled":"Enable the host firewall.","disk_encryption":"Enable full-disk encryption.","automatic_updates":"Enable automatic security updates.","screen_lock":"Require a short screen-lock timeout.","antimalware_enabled":"Enable endpoint malware protection."}
def check(snapshot: dict)->list[dict]:
    return [{"rule":"DHC001","severity":"high" if key in {"firewall_enabled","disk_encryption","antimalware_enabled"} else "medium","control":key,"message":message} for key,message in CHECKS.items() if snapshot.get(key) is not True]
def main():
    p=argparse.ArgumentParser(description="Review a desktop posture snapshot without changing the device.");p.add_argument("snapshot");a=p.parse_args()
    with open(a.snapshot,encoding="utf-8") as h:snapshot=json.load(h)
    findings=check(snapshot);print(json.dumps({"findings":findings,"finding_count":len(findings)},indent=2));raise SystemExit(1 if findings else 0)
if __name__ == "__main__":main()
