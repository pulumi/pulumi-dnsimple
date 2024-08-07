// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ZoneRecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final ZoneRecordArgs Empty = new ZoneRecordArgs();

    /**
     * The name of the record
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The name of the record
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * The priority of the record - only useful for some record types
     * 
     */
    @Import(name="priority")
    private @Nullable Output<Integer> priority;

    /**
     * @return The priority of the record - only useful for some record types
     * 
     */
    public Optional<Output<Integer>> priority() {
        return Optional.ofNullable(this.priority);
    }

    /**
     * A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
     * 
     */
    @Import(name="regions")
    private @Nullable Output<List<String>> regions;

    /**
     * @return A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
     * 
     */
    public Optional<Output<List<String>>> regions() {
        return Optional.ofNullable(this.regions);
    }

    /**
     * The TTL of the record - defaults to 3600
     * 
     */
    @Import(name="ttl")
    private @Nullable Output<Integer> ttl;

    /**
     * @return The TTL of the record - defaults to 3600
     * 
     */
    public Optional<Output<Integer>> ttl() {
        return Optional.ofNullable(this.ttl);
    }

    /**
     * The type of the record
     * 
     */
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return The type of the record
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    /**
     * The value of the record
     * 
     */
    @Import(name="value", required=true)
    private Output<String> value;

    /**
     * @return The value of the record
     * 
     */
    public Output<String> value() {
        return this.value;
    }

    /**
     * The zone name to add the record to
     * 
     */
    @Import(name="zoneName", required=true)
    private Output<String> zoneName;

    /**
     * @return The zone name to add the record to
     * 
     */
    public Output<String> zoneName() {
        return this.zoneName;
    }

    private ZoneRecordArgs() {}

    private ZoneRecordArgs(ZoneRecordArgs $) {
        this.name = $.name;
        this.priority = $.priority;
        this.regions = $.regions;
        this.ttl = $.ttl;
        this.type = $.type;
        this.value = $.value;
        this.zoneName = $.zoneName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneRecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneRecordArgs $;

        public Builder() {
            $ = new ZoneRecordArgs();
        }

        public Builder(ZoneRecordArgs defaults) {
            $ = new ZoneRecordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name The name of the record
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the record
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param priority The priority of the record - only useful for some record types
         * 
         * @return builder
         * 
         */
        public Builder priority(@Nullable Output<Integer> priority) {
            $.priority = priority;
            return this;
        }

        /**
         * @param priority The priority of the record - only useful for some record types
         * 
         * @return builder
         * 
         */
        public Builder priority(Integer priority) {
            return priority(Output.of(priority));
        }

        /**
         * @param regions A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
         * 
         * @return builder
         * 
         */
        public Builder regions(@Nullable Output<List<String>> regions) {
            $.regions = regions;
            return this;
        }

        /**
         * @param regions A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
         * 
         * @return builder
         * 
         */
        public Builder regions(List<String> regions) {
            return regions(Output.of(regions));
        }

        /**
         * @param regions A list of regions to serve the record from. You can find a list of supported values in our [developer documentation](https://developer.dnsimple.com/v2/zones/records/).
         * 
         * @return builder
         * 
         */
        public Builder regions(String... regions) {
            return regions(List.of(regions));
        }

        /**
         * @param ttl The TTL of the record - defaults to 3600
         * 
         * @return builder
         * 
         */
        public Builder ttl(@Nullable Output<Integer> ttl) {
            $.ttl = ttl;
            return this;
        }

        /**
         * @param ttl The TTL of the record - defaults to 3600
         * 
         * @return builder
         * 
         */
        public Builder ttl(Integer ttl) {
            return ttl(Output.of(ttl));
        }

        /**
         * @param type The type of the record
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The type of the record
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param value The value of the record
         * 
         * @return builder
         * 
         */
        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        /**
         * @param value The value of the record
         * 
         * @return builder
         * 
         */
        public Builder value(String value) {
            return value(Output.of(value));
        }

        /**
         * @param zoneName The zone name to add the record to
         * 
         * @return builder
         * 
         */
        public Builder zoneName(Output<String> zoneName) {
            $.zoneName = zoneName;
            return this;
        }

        /**
         * @param zoneName The zone name to add the record to
         * 
         * @return builder
         * 
         */
        public Builder zoneName(String zoneName) {
            return zoneName(Output.of(zoneName));
        }

        public ZoneRecordArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("ZoneRecordArgs", "name");
            }
            if ($.type == null) {
                throw new MissingRequiredPropertyException("ZoneRecordArgs", "type");
            }
            if ($.value == null) {
                throw new MissingRequiredPropertyException("ZoneRecordArgs", "value");
            }
            if ($.zoneName == null) {
                throw new MissingRequiredPropertyException("ZoneRecordArgs", "zoneName");
            }
            return $;
        }
    }

}
