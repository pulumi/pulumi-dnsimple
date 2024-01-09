// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.enums;

import com.pulumi.core.annotations.EnumType;
import java.lang.String;
import java.util.Objects;
import java.util.StringJoiner;

    /**
     * A DNS Record Type
     * 
     */
    @EnumType
    public enum RecordType {
        A("A"),
        AAAA("AAAA"),
        ALIAS("ALIAS"),
        CAA("CAA"),
        CNAME("CNAME"),
        HINFO("HINFO"),
        MX("MX"),
        NAPTR("NAPTR"),
        NS("NS"),
        POOL("POOL"),
        PTR("PTR"),
        SPF("SPF"),
        SRV("SRV"),
        SSHFP("SSHFP"),
        TXT("TXT"),
        URL("URL");

        private final String value;

        RecordType(String value) {
            this.value = Objects.requireNonNull(value);
        }

        @EnumType.Converter
        public String getValue() {
            return this.value;
        }

        @Override
        public String toString() {
            return new StringJoiner(", ", "RecordType[", "]")
                .add("value='" + this.value + "'")
                .toString();
        }
    }
