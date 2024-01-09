// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.dnsimple.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.dnsimple.enums.RecordType;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ZoneRecordState extends com.pulumi.resources.ResourceArgs {

    public static final ZoneRecordState Empty = new ZoneRecordState();

    @Import(name="name")
    private @Nullable Output<String> name;

    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="priority")
    private @Nullable Output<Integer> priority;

    public Optional<Output<Integer>> priority() {
        return Optional.ofNullable(this.priority);
    }

    @Import(name="qualifiedName")
    private @Nullable Output<String> qualifiedName;

    public Optional<Output<String>> qualifiedName() {
        return Optional.ofNullable(this.qualifiedName);
    }

    @Import(name="regions")
    private @Nullable Output<List<String>> regions;

    public Optional<Output<List<String>>> regions() {
        return Optional.ofNullable(this.regions);
    }

    @Import(name="ttl")
    private @Nullable Output<Integer> ttl;

    public Optional<Output<Integer>> ttl() {
        return Optional.ofNullable(this.ttl);
    }

    @Import(name="type")
    private @Nullable Output<RecordType> type;

    public Optional<Output<RecordType>> type() {
        return Optional.ofNullable(this.type);
    }

    @Import(name="value")
    private @Nullable Output<String> value;

    public Optional<Output<String>> value() {
        return Optional.ofNullable(this.value);
    }

    @Import(name="valueNormalized")
    private @Nullable Output<String> valueNormalized;

    public Optional<Output<String>> valueNormalized() {
        return Optional.ofNullable(this.valueNormalized);
    }

    @Import(name="zoneId")
    private @Nullable Output<String> zoneId;

    public Optional<Output<String>> zoneId() {
        return Optional.ofNullable(this.zoneId);
    }

    @Import(name="zoneName")
    private @Nullable Output<String> zoneName;

    public Optional<Output<String>> zoneName() {
        return Optional.ofNullable(this.zoneName);
    }

    private ZoneRecordState() {}

    private ZoneRecordState(ZoneRecordState $) {
        this.name = $.name;
        this.priority = $.priority;
        this.qualifiedName = $.qualifiedName;
        this.regions = $.regions;
        this.ttl = $.ttl;
        this.type = $.type;
        this.value = $.value;
        this.valueNormalized = $.valueNormalized;
        this.zoneId = $.zoneId;
        this.zoneName = $.zoneName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneRecordState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneRecordState $;

        public Builder() {
            $ = new ZoneRecordState();
        }

        public Builder(ZoneRecordState defaults) {
            $ = new ZoneRecordState(Objects.requireNonNull(defaults));
        }

        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder priority(@Nullable Output<Integer> priority) {
            $.priority = priority;
            return this;
        }

        public Builder priority(Integer priority) {
            return priority(Output.of(priority));
        }

        public Builder qualifiedName(@Nullable Output<String> qualifiedName) {
            $.qualifiedName = qualifiedName;
            return this;
        }

        public Builder qualifiedName(String qualifiedName) {
            return qualifiedName(Output.of(qualifiedName));
        }

        public Builder regions(@Nullable Output<List<String>> regions) {
            $.regions = regions;
            return this;
        }

        public Builder regions(List<String> regions) {
            return regions(Output.of(regions));
        }

        public Builder regions(String... regions) {
            return regions(List.of(regions));
        }

        public Builder ttl(@Nullable Output<Integer> ttl) {
            $.ttl = ttl;
            return this;
        }

        public Builder ttl(Integer ttl) {
            return ttl(Output.of(ttl));
        }

        public Builder type(@Nullable Output<RecordType> type) {
            $.type = type;
            return this;
        }

        public Builder type(RecordType type) {
            return type(Output.of(type));
        }

        public Builder value(@Nullable Output<String> value) {
            $.value = value;
            return this;
        }

        public Builder value(String value) {
            return value(Output.of(value));
        }

        public Builder valueNormalized(@Nullable Output<String> valueNormalized) {
            $.valueNormalized = valueNormalized;
            return this;
        }

        public Builder valueNormalized(String valueNormalized) {
            return valueNormalized(Output.of(valueNormalized));
        }

        public Builder zoneId(@Nullable Output<String> zoneId) {
            $.zoneId = zoneId;
            return this;
        }

        public Builder zoneId(String zoneId) {
            return zoneId(Output.of(zoneId));
        }

        public Builder zoneName(@Nullable Output<String> zoneName) {
            $.zoneName = zoneName;
            return this;
        }

        public Builder zoneName(String zoneName) {
            return zoneName(Output.of(zoneName));
        }

        public ZoneRecordState build() {
            return $;
        }
    }

}
